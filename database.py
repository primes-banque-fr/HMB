import sqlite3

conn = sqlite3.connect("data/bot.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        product TEXT,
        plan TEXT,
        amount INTEGER,
        status TEXT,
        ref TEXT
    )
    """)
    conn.commit()
