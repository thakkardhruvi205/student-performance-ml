import sqlite3

DB_NAME = "dataaaabasee.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect(DB_NAME)

    # USERS TABLE
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        department TEXT,
        team TEXT
    )
    """)

    # RESULTS TABLE
    conn.execute("""
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        skill TEXT,
        score INTEGER
    )
    """)

    # ANNOUNCEMENTS TABLE
    conn.execute("""
    CREATE TABLE IF NOT EXISTS announcements(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team TEXT,
        message TEXT,
        location TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()