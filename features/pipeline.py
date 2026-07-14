import pandas as pd

from utils.logger import feature_logger as logger

from config.config import (
    MERGED_FILE,
    CLEAN_DATA_FILE,
    FEATURE_CSV,
    FEATURE_PARQUET,
    ML_DATASET,
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

        logger.info("Starting Feature Engineering Pipeline")

        # =====================================================
        # LOAD DATASET
        # =====================================================

        print("\nLoading merged dataset...")

        df = pd.read_csv(self.input_file)

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        df = (
            df.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        print(f"Rows Loaded : {len(df):,}")
        print(f"Columns     : {len(df.columns)}")

        logger.info(
            f"Loaded {len(df):,} rows."
        )

        # =====================================================
        # REMOVE DUPLICATES
        # =====================================================

        before = len(df)

        df = df.drop_duplicates()

        duplicate_rows = before - len(df)

        before = len(df)

        df = df.drop_duplicates(
            subset=["Symbol", "Date"]
        )

        duplicate_dates = before - len(df)

        print(
            f"Duplicate Rows Removed : {duplicate_rows}"
        )

        print(
            f"Duplicate Dates Removed : {duplicate_dates}"
        )

        logger.info(
            f"Removed {duplicate_rows} duplicate rows."
        )

        logger.info(
            f"Removed {duplicate_dates} duplicate Symbol-Date rows."
        )
                # =====================================================
        # FIX NEGATIVE ADJ CLOSE
        # =====================================================

        negative_adj = (df["Adj Close"] < 0).sum()

        if negative_adj > 0:

            print(f"\nFixing {negative_adj} negative Adj Close values...")

            mask = df["Adj Close"] < 0

            df.loc[mask, "Adj Close"] = df.loc[mask, "Close"]

            logger.info(
                f"Fixed {negative_adj} negative Adj Close values."
            )

        # =====================================================
        # FIX MISSING CLOSE
        # =====================================================

        missing_close = df["Close"].isna().sum()

        if missing_close > 0:

            print(f"Fixing {missing_close} missing Close values...")

            df["Close"] = (
                df.groupby("Symbol")["Close"]
                .transform(lambda x: x.ffill().bfill())
            )

            logger.info(
                f"Fixed {missing_close} missing Close values."
            )

        # =====================================================
        # FIX MISSING ADJ CLOSE
        # =====================================================

        missing_adj = df["Adj Close"].isna().sum()

        if missing_adj > 0:

            print(f"Fixing {missing_adj} missing Adj Close values...")

            df["Adj Close"] = df["Adj Close"].fillna(df["Close"])

            logger.info(
                f"Fixed {missing_adj} missing Adj Close values."
            )

        # =====================================================
        # REMOVE INVALID PRICE ROWS
        # =====================================================

        before = len(df)

        df = df[
            (df["Open"] > 0)
            & (df["High"] > 0)
            & (df["Low"] > 0)
            & (df["Close"] > 0)
            & (df["Volume"] >= 0)
        ].copy()

        removed_invalid = before - len(df)

        if removed_invalid > 0:

            print(f"Removed {removed_invalid} invalid rows.")

            logger.info(
                f"Removed {removed_invalid} invalid rows."
            )

        # =====================================================
        # FINAL SORT AFTER CLEANING
        # =====================================================

        df = (
            df.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        print("\nData Cleaning Completed Successfully.")

        logger.info("Data Cleaning Completed Successfully.")
                # =====================================================
        # SAVE CLEAN DATASET
        # =====================================================

        print("\nSaving Clean Dataset...")

        df.to_csv(
            CLEAN_DATA_FILE,
            index=False,
            encoding="utf-8"
        )

        logger.info("Clean Dataset Saved Successfully")

        print(f"✓ Clean Dataset : {CLEAN_DATA_FILE}")

        # =====================================================
        # DATASET VALIDATION
        # =====================================================

        print("\nRunning Dataset Validation...")

        total_missing = df.isnull().sum().sum()

        total_duplicates = df.duplicated().sum()

        negative_adj = (df["Adj Close"] < 0).sum()

        invalid_high = (df["High"] < df["Low"]).sum()

        invalid_open = (
            (df["Open"] > df["High"])
            | (df["Open"] < df["Low"])
        ).sum()

        invalid_close = (
            (df["Close"] > df["High"])
            | (df["Close"] < df["Low"])
        ).sum()

        print("=" * 70)
        print("CLEAN DATA SUMMARY")
        print("=" * 70)

        print(f"Rows                : {len(df):,}")
        print(f"Columns             : {len(df.columns)}")
        print(f"Stocks              : {df['Symbol'].nunique()}")

        print()

        print(f"Missing Values      : {total_missing}")
        print(f"Duplicate Rows      : {total_duplicates}")
        print(f"Negative Adj Close  : {negative_adj}")

        print()

        print(f"Invalid High/Low    : {invalid_high}")
        print(f"Invalid Open        : {invalid_open}")
        print(f"Invalid Close       : {invalid_close}")

        logger.info(
            "Clean dataset validation completed."
        )

        print("=" * 70)
                # =====================================================
        # FEATURE ENGINEERING
        # =====================================================

        print("\nStarting Feature Engineering...")

        logger.info("Starting Technical Indicators")

        # ---------------------------------------------
        # Technical Indicators
        # ---------------------------------------------

        df = IndicatorEngine(df).calculate()

        print("✓ Technical Indicators Generated")

        logger.info("Technical Indicators Completed")

        # ---------------------------------------------
        # Volatility Features
        # ---------------------------------------------

        df = VolatilityEngine(df).calculate()

        print("✓ Volatility Indicators Generated")

        logger.info("Volatility Indicators Completed")

        # ---------------------------------------------
        # Return Features
        # ---------------------------------------------

        df = ReturnsEngine(df).calculate()

        print("✓ Return Features Generated")

        logger.info("Return Features Completed")

        # =====================================================
        # SORT DATASET
        # =====================================================

        df = (
            df.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        # =====================================================
        # SAVE FEATURE DATASET
        # =====================================================

        print("\nSaving Feature Dataset...")

        df.to_csv(
            FEATURE_CSV,
            index=False,
            encoding="utf-8"
        )

        df.to_parquet(
            FEATURE_PARQUET,
            index=False
        )

        logger.info("Feature Dataset Saved")

        print(f"✓ Feature CSV      : {FEATURE_CSV}")
        print(f"✓ Feature Parquet  : {FEATURE_PARQUET}")

        print("\nFeature Engineering Completed Successfully.")
                # =====================================================
        # CREATE ML READY DATASET
        # =====================================================

        print("\nCreating ML Ready Dataset...")

        logger.info("Creating ML Dataset")

        ml_df = df.copy()

        # ---------------------------------------------
        # Remove duplicate rows
        # ---------------------------------------------

        before_rows = len(ml_df)

        ml_df = ml_df.drop_duplicates()

        duplicate_removed = before_rows - len(ml_df)

        # ---------------------------------------------
        # Remove indicator warm-up rows
        # ---------------------------------------------

        before_rows = len(ml_df)

        ml_df = (
            ml_df
            .dropna()
            .reset_index(drop=True)
        )

        warmup_removed = before_rows - len(ml_df)

        # ---------------------------------------------
        # Final validation
        # ---------------------------------------------

        total_missing = ml_df.isnull().sum().sum()

        total_duplicates = ml_df.duplicated().sum()

        negative_adj = (ml_df["Adj Close"] < 0).sum()

        # ---------------------------------------------
        # Save ML Dataset
        # ---------------------------------------------

        ml_df.to_csv(
            ML_DATASET,
            index=False,
            encoding="utf-8"
        )

        logger.info("ML Dataset Saved Successfully")

        print(f"\n✓ ML Dataset : {ML_DATASET}")

        print(f"Rows Before Cleaning : {len(df):,}")
        print(f"Rows After Cleaning  : {len(ml_df):,}")

        print(f"Duplicate Removed    : {duplicate_removed:,}")
        print(f"Warm-up Rows Removed : {warmup_removed:,}")

        print(f"Missing Values       : {total_missing}")
        print(f"Duplicate Rows       : {total_duplicates}")
        print(f"Negative Adj Close   : {negative_adj}")
                # =====================================================
        # FINAL ASSERTIONS
        # =====================================================

        assert total_missing == 0, \
            "ML Dataset still contains missing values."

        assert total_duplicates == 0, \
            "Duplicate rows found in ML Dataset."

        assert negative_adj == 0, \
            "Negative Adj Close values still exist."

        logger.info("ML Dataset Validation Passed")

        # =====================================================
        # PIPELINE SUMMARY
        # =====================================================

        print("\n" + "=" * 70)
        print("FEATURE ENGINEERING PIPELINE COMPLETED")
        print("=" * 70)

        print("\nGenerated Files")

        print(f"✓ Clean Dataset      : {CLEAN_DATA_FILE}")
        print(f"✓ Feature CSV        : {FEATURE_CSV}")
        print(f"✓ Feature Parquet    : {FEATURE_PARQUET}")
        print(f"✓ ML Dataset         : {ML_DATASET}")

        print("\nStatistics")

        print(f"Total Stocks         : {ml_df['Symbol'].nunique()}")
        print(f"Total Rows           : {len(ml_df):,}")
        print(f"Total Columns        : {len(ml_df.columns)}")

        print("\nValidation")

        print("✓ Missing Values     : 0")
        print("✓ Duplicate Rows     : 0")
        print("✓ Negative Adj Close : 0")

        print("=" * 70)

        logger.info("Feature Pipeline Finished Successfully")

        return ml_df