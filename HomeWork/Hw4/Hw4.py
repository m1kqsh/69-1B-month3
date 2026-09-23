import asyncio
import logging
from aiogram import Bot, Dispatcher
from db import create_table
from handlers import router

TOKEN = "Токен я не хочу грубо говоря засорять дзшки токенами"


async def main():
    logging.basicConfig(level=logging.INFO)
    await create_table()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())