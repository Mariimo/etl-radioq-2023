import pandas as pd
import os 
import utils.logger as logger

def extract_data(file_path: str, sheet_name:str) -> pd.DataFrame:
    logger.log_info(f"Starting data extraction from {file_path}")
    """
    Extracts data from a excel file and returns it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the excel file.

    Returns:
    pd.DataFrame: The extracted data.
    """
    #1 Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    #2 Read the excel file
    try:
        data = pd.read_excel(file_path,sheet_name=sheet_name, engine='openpyxl')
        logger.log_info(f"Data extraction completed successfully. Extracted {len(data)} records.")

        return data   
    
    except Exception as e:
        logger.log_error(f"An error occurred while reading the data: {e}")
        raise 


