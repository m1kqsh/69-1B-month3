import aiosqlite
from queries import (
    CREATE_TABLE_USERS,
    CREATE_TABLE_RESULTS,
    SELECT_USER,
    INSERT_USER,
    SELECT_ALL_USERS,
    DELETE_USER,
    INSERT_RESULT,
    SELECT_ALL_RESULTS_WITH_USERS
)

DB_NAME = "quiz_bot.db"


async def create_tables():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(CREATE_TABLE_USERS)
        await db.execute(CREATE_TABLE_RESULTS)
        await db.commit()


async def add_user(user_id: int, username: str, first_name: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(SELECT_USER, (user_id,))
        user = await cursor.fetchone()
        if not user:
            await db.execute(INSERT_USER, (user_id, username, first_name))
            await db.commit()


async def get_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(SELECT_ALL_USERS)
        return await cursor.fetchall()


async def delete_user_db(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(DELETE_USER, (user_id,))
        await db.commit()


async def save_quiz_result(user_id: int, score: int, total: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(INSERT_RESULT, (user_id, score, total))
        await db.commit()


async def get_all_results_with_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(SELECT_ALL_RESULTS_WITH_USERS)
        return await cursor.fetchall()
