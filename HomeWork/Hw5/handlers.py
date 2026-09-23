from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from users import add_user, get_users, delete_user_db

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Без username"
    first_name = message.from_user.first_name or "Пользователь"

    await add_user(user_id, username, first_name)
    await message.answer("👋 Привет! Вы успешно добавлены в базу данных.")


@router.message(Command("users"))
async def cmd_users(message: Message):
    users = await get_users()

    if not users:
        await message.answer("В базе данных пока нет пользователей.")
        return

    response = "📋 **Список всех пользователей из БД:**\n\n"
    for u_id, u_name, f_name in users:
        response += f"• ID: `{u_id}` | Имя: {f_name} | Username: @{u_name}\n"

    await message.answer(response, parse_mode="Markdown")


@router.message(Command("delete"))
async def cmd_delete(message: Message):
    user_id = message.from_user.id
    await delete_user_db(user_id)
    await message.answer("❌ Вы успешно удалены из базы данных.")