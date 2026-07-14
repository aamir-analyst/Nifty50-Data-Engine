from pathlib import Path
import pandas as pd

from config.config import RAW_STOCK_DIR, MERGED_DIR
from utils.logger import pipeline_logger as logger

class DataMerger:

    def merge(self):

        csv_files = list(RAW_STOCK_DIR.glob("*.csv"))

        if not csv_files:
            print("❌ No CSV files found.")
            return

        all_data = []

        print("=" * 60)
        print("MERGING STOCK FILES")
        print("=" * 60)

        for file in csv_files:

            try:

                df = pd.read_csv(file)

                required_columns = [
                    "Date",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Adj Close",
                    "Volume",
                    "Symbol",
                ]

                missing = [c for c in required_columns if c not in df.columns]

                if missing:
                    print(f"⚠ Skipping {file.name}")
                    print(f"Missing Columns : {missing}")
                    continue

                df["Date"] = pd.to_datetime(df["Date"])

                all_data.append(df)

                print(f"✅ Added : {file.name}")

            except Exception as e:

                logger.error(f"{file.name} : {e}")

                print(f"❌ Error : {file.name}")

        if len(all_data) == 0:

            print("❌ No valid files found.")

            return

        merged = pd.concat(all_data, ignore_index=True)

        merged.drop_duplicates(inplace=True)

        merged.sort_values(
            by=["Symbol", "Date"],
            inplace=True
        )

        output_file = MERGED_DIR / "all_stocks.csv"

        merged.to_csv(output_file, index=False)

        print("\n" + "=" * 60)
        print("MERGE COMPLETED")
        print("=" * 60)

        print(f"Rows      : {len(merged):,}")
        print(f"Stocks    : {merged['Symbol'].nunique()}")
        print(f"Saved To  : {output_file}")