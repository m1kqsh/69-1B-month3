from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import asyncio

TOKEN = "8413452503:AAHER8WybZV-nuOFDwbEcR1Fo6-khQdoqS4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python")],
        [KeyboardButton(text="Java")],
        [KeyboardButton(text="JavaScript")],
    ],
    resize_keyboard=True,
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Выбери язык программирования:",
        reply_markup=language_keyboard
    )


descriptions = {
    "Python": "Python — простой и универсальный язык программирования, популярный в веб-разработке, анализе данных, AI и автоматизации.",
    "Java": "Java — объектно-ориентированный язык программирования, широко используемый для серверных приложений, Android и корпоративных систем.",
    "JavaScript": "JavaScript — язык программирования для веб-разработки, позволяющий создавать интерактивные элементы и приложения.",
}


@dp.message(F.text.in_(["Python", "Java", "JavaScript"]))
async def language_info(message: Message):
    await message.answer(descriptions[message.text])


@dp.message(Command("docs"))
async def docs(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Документация Python",
                    url="https://docs.python.org/3/"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Документация JS",
                    url="https://developer.mozilla.org/docs/Web/JavaScript"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Документация Java",
                    url="https://docs.oracle.com/en/java/"
                )
            ],
        ]
    )

    await message.answer(
        "Выбери язык, чтобы перейти к официальной документации:",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
