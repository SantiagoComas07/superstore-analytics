import pandas as pd
from db.db_connection import get_connection


CSV_PATH="data/processed/superstore_clean.csv"

def load_database():
    print("uploading data...")

    # Load the data 
    superstore_data = pd.read_csv(CSV_PATH)

    connection= get_connection()

    # Load database 
    superstore_data.to_sql(
        "superstore",
        connection,
        if_exists="replace",
        index=False

    )

    connection.close()

    print("Database loaded successfully")

if __name__ == "__main__":
    load_database()