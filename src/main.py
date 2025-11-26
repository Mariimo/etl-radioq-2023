from extract import extract_data
from transform import transform_data
from load import load_to_sqlite
from config.db_config import DB_path as db_path, table_name

file_path = r"D:\Fathi melondre\Data Engineer\Portofolio\radioq_etl\data\raw\Data_Radio_q.xlsx"
sheet_name = "Data Respon Pendengar 2023"

def main():
    print("[MAIN]Starting ETL Pipeline...")

    #step 1: Extract
    df = extract_data(file_path, sheet_name)
    print("[MAIN] ETL Pipeline completed successfully.")
    print(df.head()) # Display the first few rows of the DataFrame

    # step 2: Transform
    df = transform_data(df)
    print("[MAIN] Data after transformation:")

    print(df.head())  # Display the first few rows of the transformed DataFrame

    # step 3: Load
    load_to_sqlite(df, db_path , table_name)
    print("[MAIN] Load Completed.")

    #print("[DEBUG] columns.", df.columns)

if __name__ == "__main__":
    main()
