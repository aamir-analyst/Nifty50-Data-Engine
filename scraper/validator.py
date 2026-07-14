from pathlib import Path
import pandas as pd

from config.config import MERGED_DIR


class DataValidator:

    def __init__(self):
        self.file = MERGED_DIR / "all_stocks.csv"

    def run(self):

        print("=" * 70)
        print("DATA VALIDATION REPORT")
        print("=" * 70)

        df = pd.read_csv(self.file)

        print(f"Rows    : {len(df):,}")
        print(f"Columns : {len(df.columns)}")
        print(f"Stocks  : {df['Symbol'].nunique()}")

        print("\n" + "=" * 70)
        print("1. DUPLICATE CHECK")
        print("=" * 70)

        duplicates = df.duplicated().sum()
        print(f"Duplicate Rows : {duplicates}")

        print("\n" + "=" * 70)
        print("2. MISSING VALUES")
        print("=" * 70)

        print(df.isnull().sum())

        print("\n" + "=" * 70)
        print("3. PRICE VALIDATION")
        print("=" * 70)

        invalid_high = (df["High"] < df["Low"]).sum()

        invalid_open = (
            (df["Open"] > df["High"]) |
            (df["Open"] < df["Low"])
        ).sum()

        invalid_close = (
            (df["Close"] > df["High"]) |
            (df["Close"] < df["Low"])
        ).sum()

        print(f"Invalid High/Low : {invalid_high}")
        print(f"Invalid Open     : {invalid_open}")
        print(f"Invalid Close    : {invalid_close}")

        print("\n" + "=" * 70)
        print("4. VOLUME CHECK")
        print("=" * 70)

        negative_volume = (df["Volume"] < 0).sum()

        print(f"Negative Volume : {negative_volume}")

        print("\n" + "=" * 70)
        print("5. ADJ CLOSE CHECK")
        print("=" * 70)

        negative_adj = (df["Adj Close"] < 0).sum()

        print(f"Negative Adj Close : {negative_adj}")

        if negative_adj > 0:
            print("⚠ Warning: Negative Adj Close values detected.")
            print("⚠ Feature Engineering will use CLOSE price.")

        print("\n" + "=" * 70)
        print("6. DATE VALIDATION")
        print("=" * 70)

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        invalid_dates = df["Date"].isna().sum()

        print(f"Invalid Dates : {invalid_dates}")

        duplicate_dates = (
            df.groupby(["Symbol", "Date"])
              .size()
              .reset_index(name="count")
        )

        duplicate_dates = (duplicate_dates["count"] > 1).sum()

        print(f"Duplicate Dates : {duplicate_dates}")

        print("\n" + "=" * 70)
        print("7. SUMMARY")
        print("=" * 70)

        issues = (
            duplicates
            + invalid_high
            + invalid_open
            + invalid_close
            + negative_volume
            + invalid_dates
        )

        print(f"Total Issues : {issues}")

        if issues == 0:
            print("\n✅ DATASET PASSED VALIDATION")
        else:
            print("\n⚠ DATASET HAS SOME WARNINGS")

        print("=" * 70)
        print("VALIDATION COMPLETED")
        print("=" * 70)