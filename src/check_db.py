import sqlite3
import pandas as pd

conn = sqlite3.connect('data/processed/survey_2023.db')
df = pd.read_sql_query("SELECT * FROM survey_data", conn)
print(df.head())

conn.close()
