import sqlite3


DB_PATH = "db/superstore.db"


def validate_database():

    # Connect database
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    # Check tables
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    print("Tables:")
    print(tables)


    # Count rows
    cursor.execute(
        "SELECT COUNT(*) FROM superstore;"
    )

    total_rows = cursor.fetchone()[0]

    print(f"\nTotal rows: {total_rows}")


    # Show first rows
    cursor.execute(
        "SELECT * FROM superstore LIMIT 5;"
    )

    rows = cursor.fetchall()

    print("\nFirst rows:")
    for row in rows:
        print(row)


    connection.close()


if __name__ == "__main__":
    validate_database()