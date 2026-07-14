from pathlib import Path

import pandas as pd


def read_symbols(file_path: Path):

    df = pd.read_csv(file_path)

    return df["SYMBOL"].dropna().tolist()