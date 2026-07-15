import joblib
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor

from ml.dataset import DatasetLoader
from ml.target import TargetCreator
from ml.feature_selector import FeatureSelector
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
import numpy as np

from config.config import MODEL_DIR


class ModelTrainer:

    def __init__(self):

        self.model = None

        self.model_path = (
            MODEL_DIR / "random_forest.pkl"
        )

        self.feature_path = (
            MODEL_DIR / "feature_columns.pkl"
        )

    def load_dataset(self):

        print("=" * 70)
        print("MODEL TRAINING")
        print("=" * 70)

        loader = DatasetLoader()

        df = loader.prepare()

        target = TargetCreator(df)

        df = target.create()

        selector = FeatureSelector(df)

        X, y, features = selector.select()

        print("\nDataset Ready For Training")

        print(f"Rows     : {len(X):,}")

        print(f"Features : {len(features)}")

        return X, y, features
    def split_data(self):

        X, y, features = self.load_dataset()

        print("\n" + "=" * 70)
        print("TRAIN TEST SPLIT")
        print("=" * 70)

        # ==========================================
        # TIME-BASED SPLIT
        # ==========================================

        split_index = int(len(X) * 0.80)

        X_train = X.iloc[:split_index]

        X_test = X.iloc[split_index:]

        y_train = y.iloc[:split_index]

        y_test = y.iloc[split_index:]

        print(f"Training Rows : {len(X_train):,}")
        print(f"Testing Rows  : {len(X_test):,}")

        print(f"\nTraining Shape : {X_train.shape}")
        print(f"Testing Shape  : {X_test.shape}")

        print("\nTrain/Test Ratio")

        print(f"Train : {len(X_train)/len(X):.0%}")

        print(f"Test  : {len(X_test)/len(X):.0%}")

        return (
            X_train,
            X_test,
            y_train,
            y_test,
            features,
        )
    def build_model(self):

        (
            X_train,
            X_test,
            y_train,
            y_test,
            features,
        ) = self.split_data()

        print("\n" + "=" * 70)
        print("BUILDING RANDOM FOREST MODEL")
        print("=" * 70)

        # ==========================================
        # RANDOM FOREST REGRESSOR
        # ==========================================

        self.model = RandomForestRegressor(

            n_estimators=300,

            max_depth=20,

            min_samples_split=5,

            min_samples_leaf=2,

            random_state=42,

            n_jobs=-1,

            verbose=1

        )

        print("Model Configuration\n")

        print(f"Trees              : {self.model.n_estimators}")

        print(f"Maximum Depth      : {self.model.max_depth}")

        print(f"Min Samples Split  : {self.model.min_samples_split}")

        print(f"Min Samples Leaf   : {self.model.min_samples_leaf}")

        print(f"CPU Cores          : All")

        print("\nTraining Model...\n")

        self.model.fit(
            X_train,
            y_train
        )

        print("✅ Model Training Completed")

        return (
            X_train,
            X_test,
            y_train,
            y_test,
            features,
        )
    def evaluate_model(self):

        (
            X_train,
            X_test,
            y_train,
            y_test,
            features,
        ) = self.build_model()

        print("\n" + "=" * 70)
        print("MODEL EVALUATION")
        print("=" * 70)

        # ==========================================
        # PREDICTIONS
        # ==========================================

        predictions = self.model.predict(X_test)

        # ==========================================
        # METRICS
        # ==========================================

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions
            )
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        print(f"MAE  : {mae:.4f}")
        print(f"RMSE : {rmse:.4f}")
        print(f"R²   : {r2:.4f}")

        print("\nSample Predictions\n")

        preview = 10

        for actual, predicted in zip(
            y_test.iloc[:preview],
            predictions[:preview]
        ):

            print(
                f"Actual : {actual:.2f} | "
                f"Predicted : {predicted:.2f}"
            )

        return (
            predictions,
            y_test,
            features,
            mae,
            rmse,
            r2,
        )
    def save_model(self):

        (
            predictions,
            y_test,
            features,
            mae,
            rmse,
            r2,
        ) = self.evaluate_model()

        print("\n" + "=" * 70)
        print("SAVING MODEL")
        print("=" * 70)

        # ==========================================
        # SAVE RANDOM FOREST MODEL
        # ==========================================

        joblib.dump(
            self.model,
            self.model_path
        )

        print(f"✓ Model Saved : {self.model_path}")

        # ==========================================
        # SAVE FEATURE LIST
        # ==========================================

        joblib.dump(
            features,
            self.feature_path
        )

        print(f"✓ Features Saved : {self.feature_path}")

        # ==========================================
        # TRAINING SUMMARY
        # ==========================================

        print("\n" + "=" * 70)
        print("TRAINING SUMMARY")
        print("=" * 70)

        print(f"MAE        : {mae:.4f}")
        print(f"RMSE       : {rmse:.4f}")
        print(f"R² Score   : {r2:.4f}")

        print("\nModel Files")

        print(f"Random Forest : {self.model_path}")
        print(f"Features      : {self.feature_path}")

        return self.model
    def run(self):

        print("\n" + "=" * 70)
        print("STARTING MACHINE LEARNING PIPELINE")
        print("=" * 70)

        self.save_model()

        print("\n" + "=" * 70)
        print("MACHINE LEARNING PIPELINE COMPLETED")
        print("=" * 70)

        print("\nGenerated Files")

        print(f"✓ Model      : {self.model_path}")
        print(f"✓ Features   : {self.feature_path}")

        print("\nModel is Ready For Prediction.")
# ==========================================================
# TEST / ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.run()