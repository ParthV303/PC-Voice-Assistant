import sqlite3

DB_NAME = "chintu_memory.db"


def save_history(query, response):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ensure table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # insert data
    cursor.execute(
        "INSERT INTO history (query, response) VALUES (?, ?)",
        (query, response)
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT query, response FROM history ORDER BY id DESC LIMIT 5"
    )

    data = cursor.fetchall()

    conn.close()

    return data