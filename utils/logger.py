import logging
from pathlib import Path

from config.config import LOG_DIR


def get_logger(name: str):

    log_file = LOG_DIR / f"{name}.log"

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


pipeline_logger = get_logger("pipeline")
download_logger = get_logger("downloader")
validator_logger = get_logger("validator")
feature_logger = get_logger("feature_engineering")
error_logger = get_logger("error")