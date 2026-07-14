import logging

from config.config import LOG_DIR


def get_logger(name: str) -> logging.Logger:
    """
    Create or return a configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_DIR / f"{name}.log",
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


# ==========================
# Project Loggers
# ==========================

pipeline_logger = get_logger("pipeline")
download_logger = get_logger("downloader")
merger_logger = get_logger("merger")
validator_logger = get_logger("validator")
feature_logger = get_logger("feature_engineering")
error_logger = get_logger("error")

# Backward compatibility
logger = pipeline_logger