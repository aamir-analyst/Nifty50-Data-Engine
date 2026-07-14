from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA DIRECTORIES
# ==========================================================

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
RAW_STOCK_DIR = RAW_DIR / "stocks"
MERGED_DIR = RAW_DIR / "merged"
PROCESSED_DIR = DATA_DIR / "processed"
METADATA_DIR = DATA_DIR / "metadata"

DATABASE_DIR = BASE_DIR / "database"
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
MODEL_DIR = BASE_DIR / "models"

# ==========================================================
# CREATE DIRECTORIES
# ==========================================================

DIRECTORIES = [
    DATA_DIR,
    RAW_DIR,
    RAW_STOCK_DIR,
    MERGED_DIR,
    PROCESSED_DIR,
    METADATA_DIR,
    DATABASE_DIR,
    LOG_DIR,
    REPORT_DIR,
    MODEL_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# ==========================================================
# FILE PATHS
# ==========================================================

SYMBOL_FILE = METADATA_DIR / "symbols.csv"

MERGED_FILE = MERGED_DIR / "all_stocks.csv"

FEATURE_CSV = PROCESSED_DIR / "features.csv"
FEATURE_PARQUET = PROCESSED_DIR / "features.parquet"
CLEAN_DATA_FILE = PROCESSED_DIR / "clean_data.csv"

ML_DATASET = PROCESSED_DIR / "ml_dataset.csv"
DATABASE_FILE = DATABASE_DIR / "nifty.db"

VALIDATION_REPORT = REPORT_DIR / "validation_report.txt"

# ==========================================================
# DOWNLOAD SETTINGS
# ==========================================================

START_DATE = "2000-01-01"
END_DATE = "2026-12-31"

MAX_RETRIES = 5
TIMEOUT = 30
THREADS = 5

# ==========================================================
# FEATURE ENGINEERING SETTINGS
# ==========================================================

SMA_WINDOWS = [20, 50, 100, 200]

EMA_WINDOWS = [20, 50, 200]

RSI_WINDOW = 14

ATR_WINDOW = 14

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# ==========================================================
# DATABASE SETTINGS
# ==========================================================

TABLE_NAME = "stocks"

# ==========================================================
# PROJECT INFO
# ==========================================================

PROJECT_NAME = "Nifty50 Data Engine"

VERSION = "2.0.0"

AUTHOR = "Aamir"

LICENSE = "MIT"