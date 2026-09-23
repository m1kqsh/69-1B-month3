import aiosqlite
from queries import (
    CREATE_TABLE_USERS,
    SELECT_USER,
    INSERT_USER,
    SELECT_ALL_USERS,
    DELETE_USER
)

DB_NAME = "bot_database.db"


async def create_tables():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(CREATE_TABLE_USERS)
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
        users = await cursor.fetchall()
        return users


async def delete_user_db(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(DELETE_USER, (user_id,))
        await db.commit()