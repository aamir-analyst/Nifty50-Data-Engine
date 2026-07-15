import pandas as pd

from config.config import REPORT_DIR


def load_prediction_report():

    file = REPORT_DIR / "market_predictions.csv"

    if not file.exists():
        return None

    return pd.read_csv(file)