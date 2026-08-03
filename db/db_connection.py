
import sqlite3


DB_PATH="db/superstore.db"


def get_connection():
    return sqlite3.connect(DB_PATH)
