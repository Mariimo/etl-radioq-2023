📘 ETL RadioQ 2023 — End-to-End Data Engineering Pipeline

Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using Python.
The pipeline processes Radio Q’s 2023 listener survey data, cleans and standardizes the dataset, and loads it into a SQLite database for analysis and reporting.

It is designed to follow real production-style data engineering practices with:

Modular code structure

Logging

Error handling

Config separation

Database loading

Data transformations

🚀 Pipeline Architecture

Excel (.xlsx)
      |
      v
[Extract]
 - Read Excel
 - Validate path
 - Logging

      |
      v
[Transform]
 - Drop unused columns
 - Clean names
 - Normalize gender
 - Normalize city
 - Convert age → integer
 - Create age_group
 - Rename columns
 - Deduplicate rows
 - Convert to snake_case
 - Logging per step

      |
      v
[Load]
 - Insert into SQLite
 - Create table "survey_data"
 - Save into processed DB
 - Logging

📂 Project Structure

etl-radioq-2023/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── utils/
│       └── logger.py
│
├── config/
│   └── db_config.py
│
├── data/
│   ├── raw/
│   │   └── Data_Radio_q.xlsx
│   └── processed/
│       └── survey_2023.db
│
├── logs/
│   └── etl_logs.log
│
├── requirements.txt
└── README.md

⚙️ How to Run the Pipeline

1. Clone the repository
2. Install dependencies
3. Run the ETL pipeline
4. Verify the SQLite database

🧹 Transformations Applied

🔹 Drop unnecessary columns
No and other irrelevant fields.

🔹 Clean respondent names
- Remove titles (Dr, Ir, S.H, M.Pd, etc.)
- Trim whitespace
- Standardize casing

🔹 Normalize gender values
Convert variations like:
- “pria”, “cowok”, “jantan” → Laki-laki
- “wanita”, “cewek” → Perempuan

🔹 Normalize city names
- Convert inconsistent casing and spacing.

🔹 Convert age → integer
- With safe coercion for invalid values.

🔹 Create age groups
- < 18 → Anak-anak
- 18–30 → Dewasa Muda
- 31–50 → Dewasa
- 50 → Lansia

🔹 Rename columns
- “Bulan” → “Bulan Survey”
- “Asal” → “Asal Pendengar”

🔹 Convert all column names → snake_case

🗄️ Load Layer
Data is written into:
data/processed/survey_2023.db

Loaded table:
- survey_data
with all cleaned & transformed fields.

📜 Tech Stack
- Python
- Pandas
- SQLite
- Logging
- Modular ETL architecture

🧑‍💻 Author
Fathi Melondre Putra
Data Engineering / Data Analytics
