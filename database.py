import sqlite3

conn = sqlite3.connect("wellness.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS moods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mood TEXT
)
""")

conn.commit()

print("Database Created Successfully")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")