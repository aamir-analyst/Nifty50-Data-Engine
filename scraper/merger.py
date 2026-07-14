from pathlib import Path

import pandas as pd

from config.config import (
    RAW_STOCK_DIR,
    MERGED_DIR,
)

from utils.logger import (
    pipeline_logger as logger
)


class DataMerger:

    def __init__(self):

        self.input_dir = RAW_STOCK_DIR

        self.output_file = (
            MERGED_DIR / "all_stocks.csv"
        )

    def merge(self):

        csv_files = sorted(
            self.input_dir.glob("*.csv")
        )

        if not csv_files:

            print("❌ No CSV files found.")

            logger.error(
                "No CSV files found."
            )

            return

        print("=" * 70)
        print("MERGING STOCK FILES")
        print("=" * 70)

        logger.info(
            f"{len(csv_files)} CSV files found."
        )

        all_data = []
                # =====================================================
        # READ ALL STOCK FILES
        # =====================================================

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

        for file in csv_files:

            try:

                print(f"Reading : {file.name}")

                df = pd.read_csv(file)

                # ---------------------------------------------
                # Validate Required Columns
                # ---------------------------------------------

                missing_columns = [
                    col
                    for col in required_columns
                    if col not in df.columns
                ]

                if missing_columns:

                    print(
                        f"⚠ Skipped : {file.name}"
                    )

                    print(
                        f"Missing Columns : {missing_columns}"
                    )

                    logger.warning(
                        f"{file.name} missing columns : {missing_columns}"
                    )

                    continue

                # ---------------------------------------------
                # Date Conversion
                # ---------------------------------------------

                df["Date"] = pd.to_datetime(
                    df["Date"],
                    errors="coerce"
                )

                # Remove invalid dates

                df = df.dropna(
                    subset=["Date"]
                )

                # Sort stock data

                df = (
                    df.sort_values("Date")
                    .reset_index(drop=True)
                )

                all_data.append(df)

                print(
                    f"✓ Added : {file.name} ({len(df):,} rows)"
                )

                logger.info(
                    f"{file.name} added successfully."
                )

            except Exception as e:

                print(
                    f"❌ Error : {file.name}"
                )

                logger.exception(e)
                        # =====================================================
        # MERGE ALL DATA
        # =====================================================

        if len(all_data) == 0:

            print("\n❌ No valid CSV files found.")

            logger.error("No valid CSV files found.")

            return

        print("\nMerging datasets...")

        merged = pd.concat(
            all_data,
            ignore_index=True
        )

        logger.info(
            f"Merged Rows : {len(merged):,}"
        )

        # =====================================================
        # SORT DATA
        # =====================================================

        merged = (
            merged.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        # =====================================================
        # REMOVE DUPLICATES
        # =====================================================

        before_rows = len(merged)

        merged = merged.drop_duplicates(
            subset=["Symbol", "Date"],
            keep="last"
        )

        duplicate_removed = (
            before_rows - len(merged)
        )

        # =====================================================
        # FINAL SORT
        # =====================================================

        merged = (
            merged.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        logger.info(
            f"Duplicate Symbol-Date Removed : {duplicate_removed:,}"
        )

        print(
            f"\nDuplicate Symbol-Date Removed : {duplicate_removed:,}"
        )

        # =====================================================
        # FINAL VALIDATION
        # =====================================================

        duplicate_rows = merged.duplicated().sum()

        duplicate_symbol_date = merged.duplicated(
            subset=["Symbol", "Date"]
        ).sum()

        print("\nValidation")

        print(
            f"Duplicate Rows        : {duplicate_rows}"
        )

        print(
            f"Duplicate Symbol-Date : {duplicate_symbol_date}"
        )

        logger.info(
            "Validation Completed Successfully."
        )
                # =====================================================
        # SAVE MERGED DATASET
        # =====================================================

        print("\nSaving merged dataset...")

        merged.to_csv(
            self.output_file,
            index=False,
            encoding="utf-8"
        )

        logger.info(
            f"Merged dataset saved : {self.output_file}"
        )

        # =====================================================
        # FINAL SUMMARY
        # =====================================================

        print("\n" + "=" * 70)
        print("MERGE COMPLETED")
        print("=" * 70)

        print(f"Total Stocks            : {merged['Symbol'].nunique()}")
        print(f"Total Rows              : {len(merged):,}")
        print(f"Total Columns           : {len(merged.columns)}")

        print()

        print(f"Duplicate Rows Removed  : {duplicate_removed:,}")

        print(
            f"Trading Date Range      : "
            f"{merged['Date'].min().date()}  →  "
            f"{merged['Date'].max().date()}"
        )

        print()

        print(f"Saved To                : {self.output_file}")

        print("=" * 70)

        logger.info("Data Merge Completed Successfully.")

        return merged