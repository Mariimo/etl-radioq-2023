import pandas as pd
import utils.logger as logger

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.log_info("Starting data transformation.")

    """
    Transforms the input DataFrame by cleaning and formatting the data.

    Parameters:
    df (pd.DataFrame): The input DataFrame to be transformed.

    Returns:
    pd.DataFrame: The transformed DataFrame.
    """
     # 1. Drop unnecessary columns
    logger.log_info("Dropping unnecessary columns.")
    columns_to_drop = ['No']  # Replace with actual column names
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])


    # 2. Clean names (remove titles, trim spaces, proper case)
    logger.log_info("Cleaning names.")
    def clean_name(name):
        if pd.isna(name):
            return None
        # Remove common titles
        titles = ["Dr", "Ir", "H", "S.H", "M.Pd", "A.Md", "M.Kom", "dkk", "Dra", "Dr .", "dr .","Ir . ","Dr.","dr.","Ir.","Dr. ","Ir. ", ".",","]
        for t in titles:
            name = name.replace(t, '')
        # Trim spaces and convert to proper case
        name = ' '.join(name.split()).title()
        return name.title()
    
    if "Nama Depan" in df.columns:
        df["Nama Depan"] = df["Nama Depan"].apply(clean_name)


    # 3. Normalize gender values
    logger.log_info("Normalizing gender.")
    def normalize_gender(x):
        x= str(x).strip().lower()
        if x in ["pria", "laki-laki", "cowok", "lelaki", "Jantan","Pria"]:
            return "Laki-laki"
        elif x in ["wanita", "perempuan", "cewek","betina","Wanita"]:
            return "Perempuan"
        else:
            return None

    if "Jenis Kelamin" in df.columns:
        df["Jenis Kelamin"] = df["Jenis Kelamin"].apply(normalize_gender)



    # 4. Normalize city column
    logger.log_info("Normalizing city names.")
    if "Asal" in df.columns:
        df["Asal"] = df["Asal"].astype(str).str.strip().str.title()


    # 5. Convert age to integer
    logger.log_info("Converting age to integer.")
    if "Umur" in df.columns:
        df["Umur"] = pd.to_numeric(df["Umur"], errors="coerce").astype("Int64")

    # 6. Create age_group column
    logger.log_info("Creating age group column.")
    def age_group(age):
        if pd.isna(age):
            return None
        if age < 18:
            return "Anak - anak"
        elif age <= 30:
            return "Dewasa Muda"
        elif age <= 50:
            return "Dewasa"
        else:
            return "Lansia"
            
    df["age_group"] = df["Umur"].apply(age_group)

    # 7. Kolom bulan kita ubah namanya
    logger.log_info("Renaming month column.")
    if "Bulan" in df.columns:
        df = df.rename(columns={"Bulan": "Bulan Survey"}) 

    # ganti nama kolom asal
    logger.log_info("Renaming origin column.")
    if "Asal" in df.columns:
        df = df.rename(columns={"Asal": "Asal Pendengar"})
    # 8. Drop duplicates
    df = df.drop_duplicates()

    # 9. Rename columns to snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")




    print("[transform] Data successfully transformed.")
    return df