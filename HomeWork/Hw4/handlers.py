from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from db import QUIZ_DATA, get_quiz_index, update_quiz_index, get_quiz_score
from keyboards import get_answer_keyboard, get_restart_keyboard

router = Router()


async def send_question(message_or_query, user_id: int):
    current_index = await get_quiz_index(user_id)
    question_data = QUIZ_DATA[current_index]
    keyboard = get_answer_keyboard(question_data["options"])

    text = f"📌 **Вопрос {current_index + 1} из {len(QUIZ_DATA)}**\n\n{question_data['question']}"

    if isinstance(message_or_query, Message):
        await message_or_query.answer(text, reply_markup=keyboard, parse_mode="Markdown")
    else:
        await message_or_query.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await update_quiz_index(message.from_user.id, index=0, score=0)
    await message.answer(
        "👋 **Добро пожаловать в итоговую викторину по курсу!**\nТемы: Ubuntu, aiogram, FSM, SQL (CRUD, JOIN, GROUP BY).")
    await send_question(message, message.from_user.id)


@router.callback_query(F.data == "start_quiz")
async def cb_start_quiz(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await update_quiz_index(callback.from_user.id, index=0, score=0)
    await send_question(callback, callback.from_user.id)
    await callback.answer()


@router.callback_query(F.data.startswith("ans_"))
async def handle_answer(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    selected_option = int(callback.data.split("_")[1])

    current_index = await get_quiz_index(user_id)
    current_score = await get_quiz_score(user_id)
    question_data = QUIZ_DATA[current_index]

    if selected_option == question_data["correct"]:
        current_score += 1
        await callback.answer("Верно! ✅")
    else:
        correct_text = question_data["options"][question_data["correct"]]
        await callback.answer(f"Неверно! ❌ Правильный ответ: {correct_text}", show_alert=True)

    next_index = current_index + 1
    if next_index >= len(QUIZ_DATA):
        await state.clear()

        total = len(QUIZ_DATA)
        result_text = (
            f"🏁 **Викторина завершена!**\n\n"
            f"Твой результат: **{current_score}** из **{total}** правильных ответов.\n"
        )
        if current_score == total:
            result_text += "🏆 Отличная работа! Отличный уровень знаний."
        elif current_score >= total // 2:
            result_text += "👍 Хороший результат! Но есть что повторить."
        else:
            result_text += "📚 Рекомендуется повторить пройденный материал."

        await callback.message.edit_text(
            result_text,
            reply_markup=get_restart_keyboard(),
            parse_mode="Markdown"
        )
    else:
        await update_quiz_index(user_id, index=next_index, score=current_score)
        await send_question(callback, user_id)