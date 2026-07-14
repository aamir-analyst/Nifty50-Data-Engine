import pandas as pd

from config.config import (
    MERGED_FILE,
    FEATURE_CSV,
    FEATURE_PARQUET,
)

from features.indicators import IndicatorEngine
from features.volatility import VolatilityEngine
from features.returns import ReturnsEngine


class FeaturePipeline:

    def __init__(self):

        self.input_file = MERGED_FILE

    def run(self):

        print("=" * 70)
        print("FEATURE ENGINEERING PIPELINE")
        print("=" * 70)

        # ----------------------------
        # Load Dataset
        # ----------------------------

        df = pd.read_csv(self.input_file)

        df["Date"] = pd.to_datetime(df["Date"])

        df = df.sort_values(
            ["Symbol", "Date"]
        )

        print(f"Loaded Rows : {len(df):,}")

        # ----------------------------
        # Indicators
        # ----------------------------

        df = IndicatorEngine(df).calculate()

        # ----------------------------
        # Volatility
        # ----------------------------

        df = VolatilityEngine(df).calculate()

        # ----------------------------
        # Returns
        # ----------------------------

        df = ReturnsEngine(df).calculate()

        # ----------------------------
        # Remove duplicate rows
        # ----------------------------

        df = df.drop_duplicates()

        # ----------------------------
        # Sort
        # ----------------------------

        df = df.sort_values(
            ["Symbol", "Date"]
        )

        # ----------------------------
        # Save CSV
        # ----------------------------

        df.to_csv(
            FEATURE_CSV,
            index=False
        )

        # ----------------------------
        # Save Parquet
        # ----------------------------

        df.to_parquet(
            FEATURE_PARQUET,
            index=False
        )

        print("\n" + "=" * 70)
        print("FEATURE ENGINEERING COMPLETED")
        print("=" * 70)

        print(f"Rows    : {len(df):,}")
        print(f"Columns : {len(df.columns)}")

        print(f"\nCSV Saved      : {FEATURE_CSV}")
        print(f"Parquet Saved  : {FEATURE_PARQUET}")

        return df