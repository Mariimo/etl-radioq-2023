import logging
import os

# Create logs directory if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=f"{LOG_DIR}/etl_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message: str):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message: str):
    logging.error(message)
    print(f"[ERROR] {message}")

def log_warning(message: str):
    logging.warning(message)
    print(f"[WARNING] {message}")
