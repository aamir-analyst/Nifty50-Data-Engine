import pandas as pd

from config.config import ML_DATASET


class DatasetLoader:

    def __init__(self):

        self.file = ML_DATASET

    def load(self):

        print("=" * 70)
        print("LOADING ML DATASET")
        print("=" * 70)

        df = pd.read_csv(self.file)

        print(f"Rows    : {len(df):,}")
        print(f"Columns : {len(df.columns)}")

        return df
    def prepare(self):

         df = self.load()

         print("\nPreparing Dataset...")

        # ==========================================
        # DATE CONVERSION
        # ==========================================

         df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        # ==========================================
        # REMOVE INVALID DATES
        # ==========================================

         before = len(df)

         df = df.dropna(
            subset=["Date"]
        )

         invalid_dates = before - len(df)

        # ==========================================
        # SORT DATA
        # ==========================================

         df = (
            df.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        # ==========================================
        # REMOVE DUPLICATES
        # ==========================================

         before = len(df)

         df = df.drop_duplicates()

         duplicate_rows = before - len(df)

        # ==========================================
        # MISSING VALUES
        # ==========================================

         missing = df.isnull().sum().sum()

         print(f"Invalid Dates    : {invalid_dates}")
         print(f"Duplicate Rows   : {duplicate_rows}")
         print(f"Missing Values   : {missing}")

         return df
            # ==========================================
        # FINAL DATASET SUMMARY
        # ==========================================

         print("\n" + "=" * 70)
         print("ML DATASET SUMMARY")
         print("=" * 70)

         print(f"Rows               : {len(df):,}")
         print(f"Columns            : {len(df.columns)}")
         print(f"Stocks             : {df['Symbol'].nunique()}")

         print(
            f"Date Range         : "
            f"{df['Date'].min().date()}  →  "
            f"{df['Date'].max().date()}"
        )

         print(f"Missing Values     : {df.isnull().sum().sum()}")
         print(f"Duplicate Rows     : {df.duplicated().sum()}")

         print("=" * 70)
         print("ML DATASET READY")
         print("=" * 70)

         return df


if __name__ == "__main__":

    loader = DatasetLoader()

    df = loader.prepare()

    print("\nPreview\n")

    print(df.head())