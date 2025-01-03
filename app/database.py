import aiosqlite as sq
import os

# Укажите путь к вашей базе данных
DB_NAME = os.path.join('instance', 'database.db')


async def create_db():
    async with sq.connect(DB_NAME) as db:
        print("Database created!")

        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )""")

        await db.execute("""CREATE TABLE IF NOT EXISTS texts (
            text_id INTEGER PRIMARY KEY,
            title TEXT,
            main_text TEXT
        )""")

        await db.commit()


async def insert_user(user_id, username):
    async with sq.connect(DB_NAME) as db:
        await db.execute("INSERT OR REPLACE INTO users VALUES (?, ?)", (user_id, username))
        await db.commit()


async def get_main_text_by_text_id(text_id):
    async with sq.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM texts WHERE text_id = ?", (text_id,)) as cursor:
            return await cursor.fetchone()