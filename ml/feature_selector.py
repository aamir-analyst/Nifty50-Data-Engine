import pandas as pd


class FeatureSelector:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    def select(self):

        print("=" * 70)
        print("FEATURE SELECTION")
        print("=" * 70)

        df = self.df.copy()

        # ==========================================
        # EXCLUDED COLUMNS
        # ==========================================

        excluded_columns = [
            "Date",
            "Symbol",
            "TARGET",
            "Adj Close",

        ]

        # ==========================================
        # FEATURE COLUMNS
        # ==========================================

        feature_columns = [
            col
            for col in df.columns
            if col not in excluded_columns
        ]

        print(f"Total Features : {len(feature_columns)}")
            # ==========================================
        # CREATE FEATURE MATRIX (X)
        # ==========================================

        X = df[feature_columns].copy()

        # ==========================================
        # CREATE TARGET VECTOR (y)
        # ==========================================

        y = df["TARGET"].copy()

        print(f"Feature Matrix Shape : {X.shape}")
        print(f"Target Shape         : {y.shape}")

        # ==========================================
        # FEATURE LIST
        # ==========================================

        print("\nSelected Features\n")

        for feature in feature_columns:

            print(f"✓ {feature}")
            # ==========================================
        # DATA TYPE VALIDATION
        # ==========================================

        print("\nValidating Feature Data Types...\n")

        non_numeric = []

        for column in feature_columns:

            if not pd.api.types.is_numeric_dtype(X[column]):

                non_numeric.append(column)

        if non_numeric:

            print("❌ Non-Numeric Features Found")

            for col in non_numeric:

                print(f"   - {col}")

            raise ValueError(
                "Feature matrix contains non-numeric columns."
            )

        print("✅ All Features Are Numeric")

        # ==========================================
        # TARGET VALIDATION
        # ==========================================

        if y.isnull().sum() > 0:

            raise ValueError(
                "Target contains missing values."
            )

        print("✅ Target Validation Passed")

        # ==========================================
        # FEATURE SUMMARY
        # ==========================================

        print("\n" + "=" * 70)
        print("FEATURE SELECTION COMPLETED")
        print("=" * 70)

        print(f"Final Features : {len(feature_columns)}")
        print(f"Training Rows  : {len(X):,}")

        print("=" * 70)
            # ==========================================
        # RETURN TRAINING DATA
        # ==========================================

        return X, y, feature_columns


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    from ml.dataset import DatasetLoader
    from ml.target import TargetCreator

    # Load Dataset
    loader = DatasetLoader()
    df = loader.prepare()

    # Create Target
    target = TargetCreator(df)
    df = target.create()

    # Select Features
    selector = FeatureSelector(df)

    X, y, features = selector.select()

    print("\n" + "=" * 70)
    print("FEATURE SELECTION TEST")
    print("=" * 70)

    print(f"X Shape : {X.shape}")
    print(f"y Shape : {y.shape}")

    print("\nFirst 10 Features\n")

    for feature in features[:10]:
        print(f"✓ {feature}")

    print("\nTarget Preview\n")

    print(y.head())