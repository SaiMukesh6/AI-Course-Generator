import sqlite3

DATABASE_NAME = "data/courses.db"


def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_course(topic, course):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (topic, course) VALUES (?, ?)",
        (topic, course)
    )

    conn.commit()
    conn.close()


def get_courses():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT topic, course FROM courses ORDER BY id DESC")

    courses = cursor.fetchall()

    conn.close()

    return courses


def delete_all_courses():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM courses")

    conn.commit()
    conn.close()