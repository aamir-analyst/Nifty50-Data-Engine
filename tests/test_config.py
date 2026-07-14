from config.config import (
    DATA_DIR,
    RAW_STOCK_DIR,
    MERGED_DIR,
    DATABASE_FILE,
)


def test_directories_exist():

    assert DATA_DIR.exists()
    assert RAW_STOCK_DIR.exists()
    assert MERGED_DIR.exists()


def test_database_path():

    assert DATABASE_FILE.name == "nifty.db"