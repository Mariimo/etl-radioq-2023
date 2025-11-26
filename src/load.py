import sqlite3
import pandas as pd
import os

def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: "survey_data"):
    """
    Loads the given DataFrame into a SQLite database table.

    Parameters:
    df (pd.DataFrame): The DataFrame to be loaded.
    db_path (str): The path to the SQLite database file.
    table_name (str): The name of the table to load data into.
    """
    # 1. Ensure the database directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # 2. Connect to the SQLite database (it will be created if it doesn't exist)
    print("[DEBUG] writing to",os.path.abspath(db_path))
    conn = sqlite3.connect(db_path)
    
    
     # 3. Load DataFrame into the specified table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
       
    # 4. Close the database connection
    conn.close()

    print(f"[LOAD] Data successfully loaded into {db_path} in table '{table_name}'.")

