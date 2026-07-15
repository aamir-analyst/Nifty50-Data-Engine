import pandas as pd


class TargetCreator:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    def create(self):

        print("=" * 70)
        print("CREATING TARGET VARIABLE")
        print("=" * 70)

        df = self.df.copy()

        # ==========================================
        # SORT DATASET
        # ==========================================

        df = (
            df.sort_values(
                ["Symbol", "Date"]
            )
            .reset_index(drop=True)
        )

        print(f"Rows Before Target : {len(df):,}")

        # ==========================================
        # CREATE TARGET COLUMN
        # ==========================================

        print("\nCreating Tomorrow Close Target...")

        df["TARGET"] = (
            df.groupby("Symbol")["Close"]
              .shift(-1)
        )

        target_missing = df["TARGET"].isna().sum()

        print(f"Target Missing Rows : {target_missing:,}")

        # ==========================================
        # REMOVE LAST ROW OF EACH STOCK
        # ==========================================

        before_rows = len(df)

        df = (
            df.dropna(subset=["TARGET"])
              .reset_index(drop=True)
        )

        removed_rows = before_rows - len(df)

        print(f"Rows Removed : {removed_rows:,}")

        print(f"Rows After Target : {len(df):,}")

        # ==========================================
        # TARGET VALIDATION
        # ==========================================

        print("\nValidating Target...")

        target_missing = df["TARGET"].isnull().sum()

        print(f"Missing Target Values : {target_missing}")

        print("\nTarget Statistics")

        print(f"Minimum Target : {df['TARGET'].min():.2f}")
        print(f"Maximum Target : {df['TARGET'].max():.2f}")
        print(f"Average Target : {df['TARGET'].mean():.2f}")

        print("\n" + "=" * 70)
        print("TARGET CREATED SUCCESSFULLY")
        print("=" * 70)

        print(f"Final Rows    : {len(df):,}")
        print(f"Final Columns : {len(df.columns)}")

        # ==========================================
        # FINAL CHECK
        # ==========================================

        print("\nDataset Preview\n")

        print(
            df[
                [
                    "Date",
                    "Symbol",
                    "Close",
                    "TARGET",
                ]
            ].head()
        )
        return df


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    from ml.dataset import DatasetLoader

    loader = DatasetLoader()

    df = loader.prepare()

    target = TargetCreator(df)

    df = target.create()

    print("\nTarget Dataset Shape")

    print(df.shape)