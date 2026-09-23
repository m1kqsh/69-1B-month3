import asyncio
import logging
from aiogram import Bot, Dispatcher
from users import create_tables
from handlers import router

TOKEN = "ВАШ_ТОКЕН_БОТА"


async def main():
    logging.basicConfig(level=logging.INFO)

    await create_tables()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())