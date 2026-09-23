import aiosqlite
QUIZ_DATA = [
    {
        "question": "1. [Ubuntu] Какая команда используется для обновления списка пакетов в Ubuntu?",
        "options": ["sudo apt update", "sudo apt upgrade", "apt-get install", "systemctl update"],
        "correct": 0
    },
    {
        "question": "2. [aiogram] Какой класс в aiogram отвечает за отслеживание состояний пользователя?",
        "options": ["Router", "FSMContext", "Dispatcher", "Bot"],
        "correct": 1
    },
    {
        "question": "3. [Callback & FSM] Каким методом сбрасывается текущее состояние FSM?",
        "options": ["state.reset()", "state.clear()", "state.finish()", "state.delete()"],
        "correct": 1
    },
    {
        "question": "4. [Проектирование БД] Какой ключ используется для связи двух таблиц между собой?",
        "options": ["Primary Key (Первичный)", "Foreign Key (Внешний)", "Unique Key", "Index Key"],
        "correct": 1
    },
    {
        "question": "5. [SQL CRUD] Какая команда отвечает за изменение существующих записей в таблице?",
        "options": ["INSERT", "SELECT", "UPDATE", "MODIFY"],
        "correct": 2
    },
    {
        "question": "6. [SQL JOIN] Какой JOIN возвращает все строки из левой таблицы и совпадающие строки из правой?",
        "options": ["INNER JOIN", "RIGHT JOIN", "FULL JOIN", "LEFT JOIN"],
        "correct": 3
    },
    {
        "question": "7. [SQL GROUP BY/HAVING] В чем отличие HAVING от WHERE?",
        "options": [
            "HAVING фильтрует данные ПОСЛЕ группировки (агрегации)",
            "WHERE работает быстрее, чем HAVING в любых условиях",
            "HAVING используется только с текстовыми полями",
            "Они абсолютно идентичны"
        ],
        "correct": 0
    },
    {
        "question": "8. [SQL] Какая агрегатная функция подсчитывает количество строк в запросе?",
        "options": ["SUM()", "COUNT()", "TOTAL()", "AVG()"],
        "correct": 1
    },
    {
        "question": "9. [Итоговый тест] Как называется архитектурный подход к асинхронной обработке событий в aiogram?",
        "options": ["Event Loop", "Multi-threading", "Polymorphism", "Blocking I/O"],
        "correct": 0
    },
    {
        "question": "10. [Итоговый тест] Что произойдет при выполнении 'DELETE FROM users;' без условия WHERE?",
        "options": [
            "Удалится только первая строка",
            "Удалятся все строки из таблицы users",
            "База данных выдаст ошибку",
            "Таблица удалится полностью вместе со структурой"
        ],
        "correct": 1
    }
]

DB_NAME = 'quiz_bot.db'

async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS quiz_state (
                user_id INTEGER PRIMARY KEY,
                question_index INTEGER,
                score INTEGER
            )
        ''')
        await db.commit()

async def get_quiz_index(user_id: int) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def update_quiz_index(user_id: int, index: int, score: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            'INSERT OR REPLACE INTO quiz_state (user_id, question_index, score) VALUES (?, ?, ?)',
            (user_id, index, score)
        )
        await db.commit()

async def get_quiz_score(user_id: int) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT score FROM quiz_state WHERE user_id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0