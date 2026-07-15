import joblib
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error,
)

from config.config import MODEL_DIR, EVALUATION_DIR
from ml.dataset import DatasetLoader
from ml.target import TargetCreator
from ml.feature_selector import FeatureSelector


class ModelEvaluator:

    def __init__(self):

        self.model = joblib.load(
            MODEL_DIR / "random_forest.pkl"
        )

        self.features = joblib.load(
            MODEL_DIR / "feature_columns.pkl"
        )

        # Global Chart Style
        plt.style.use("ggplot")

        plt.rcParams.update({

            "font.size": 14,

            "axes.titlesize": 18,

            "axes.labelsize": 15,

            "xtick.labelsize": 12,

            "ytick.labelsize": 12,

            "legend.fontsize": 12,

            "figure.dpi": 150

        })

    def load_dataset(self):

        print("=" * 70)
        print("MODEL EVALUATION")
        print("=" * 70)

        loader = DatasetLoader()

        df = loader.prepare()

        df = TargetCreator(df).create()

        X, y, _ = FeatureSelector(df).select()

        return X, y

    def evaluate(self):

        X, y = self.load_dataset()

        print("\n" + "=" * 70)
        print("RUNNING MODEL EVALUATION")
        print("=" * 70)

        split = int(len(X) * 0.80)

        X_test = X.iloc[split:]
        y_test = y.iloc[split:]

        predictions = self.model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)

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

        mape = (
            mean_absolute_percentage_error(
                y_test,
                predictions
            )
            * 100
        )

        print(f"MAE  : {mae:.4f}")
        print(f"RMSE : {rmse:.4f}")
        print(f"R²   : {r2:.4f}")
        print(f"MAPE : {mape:.2f}%")

        return (
            X_test,
            y_test,
            predictions,
            mae,
            rmse,
            r2,
            mape
        )

    def feature_importance(self):

        (
            X_test,
            y_test,
            predictions,
            mae,
            rmse,
            r2,
            mape
        ) = self.evaluate()

        importance = pd.DataFrame({

            "Feature": self.features,

            "Importance": self.model.feature_importances_

        })

        importance = (

            importance

            .sort_values(

                by="Importance",

                ascending=False

            )

            .reset_index(drop=True)

        )

        print("\nTop 10 Features\n")

        print(

            importance.head(10)

        )

        return (

            importance,

            X_test,

            y_test,

            predictions,

            mae,

            rmse,

            r2,

            mape

        )
def create_visualizations(self):

    (
        importance,
        X_test,
        y_test,
        predictions,
        mae,
        rmse,
        r2,
        mape,
    ) = self.feature_importance()

    print("\n" + "=" * 70)
    print("CREATING VISUALIZATIONS")
    print("=" * 70)

    # ======================================================
    # FEATURE IMPORTANCE
    # ======================================================

    top10 = importance.head(10)

    plt.figure(figsize=(10, 5))

    plt.barh(
        top10["Feature"],
        top10["Importance"],
        color="royalblue"
    )

    plt.gca().invert_yaxis()

    plt.title(
        "Top 10 Important Features",
        fontsize=18,
        weight="bold"
    )

    plt.xlabel(
        "Importance",
        fontsize=14
    )

    plt.grid(axis="x", alpha=.30)

    plt.tight_layout()

    feature_plot = (
        EVALUATION_DIR /
        "feature_importance.png"
    )

    plt.savefig(
        feature_plot,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"✓ Saved : {feature_plot}")

    # ======================================================
    # ACTUAL VS PREDICTED
    # ======================================================

    sample = 150

    plt.figure(figsize=(10,5))

    plt.plot(

        y_test.iloc[:sample].values,

        linewidth=2,

        label="Actual",

        color="green"

    )

    plt.plot(

        predictions[:sample],

        linewidth=2,

        label="Predicted",

        color="red"

    )

    plt.title(

        "Actual vs Predicted Prices",

        fontsize=18,

        weight="bold"

    )

    plt.xlabel("Samples")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(alpha=.3)

    plt.tight_layout()

    prediction_plot = (

        EVALUATION_DIR /

        "actual_vs_predicted.png"

    )

    plt.savefig(

        prediction_plot,

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    print(f"✓ Saved : {prediction_plot}")

    return (

        importance,

        y_test,

        predictions,

        mae,

        rmse,

        r2,

        mape,

    )
def create_reports(self):

    (
        importance,
        y_test,
        predictions,
        mae,
        rmse,
        r2,
        mape,
    ) = self.create_visualizations()

    print("\n" + "=" * 70)
    print("CREATING EVALUATION REPORTS")
    print("=" * 70)

    residuals = y_test.values - predictions

    # ======================================================
    # RESIDUAL PLOT
    # ======================================================

    plt.figure(figsize=(10,5))

    plt.scatter(

        predictions,

        residuals,

        s=20,

        alpha=0.55,

        color="royalblue"

    )

    plt.axhline(

        y=0,

        color="red",

        linestyle="--",

        linewidth=2

    )

    plt.title(

        "Residual Plot",

        fontsize=18,

        weight="bold"

    )

    plt.xlabel("Predicted Price")

    plt.ylabel("Residual")

    plt.grid(alpha=.30)

    plt.tight_layout()

    residual_plot = (

        EVALUATION_DIR /

        "residual_plot.png"

    )

    plt.savefig(

        residual_plot,

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    print(f"✓ Saved : {residual_plot}")

    # ======================================================
    # ERROR DISTRIBUTION
    # ======================================================

    plt.figure(figsize=(10,5))

    plt.hist(

        residuals,

        bins=40,

        color="royalblue",

        edgecolor="black"

    )

    plt.title(

        "Prediction Error Distribution",

        fontsize=18,

        weight="bold"

    )

    plt.xlabel("Prediction Error")

    plt.ylabel("Frequency")

    plt.grid(alpha=.25)

    plt.tight_layout()

    error_plot = (

        EVALUATION_DIR /

        "error_distribution.png"

    )

    plt.savefig(

        error_plot,

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    print(f"✓ Saved : {error_plot}")

    # ======================================================
    # METRICS CSV
    # ======================================================

    metrics = pd.DataFrame({

        "Metric":[

            "MAE",

            "RMSE",

            "R2",

            "MAPE"

        ],

        "Value":[

            mae,

            rmse,

            r2,

            mape

        ]

    })

    metrics_file = (

        EVALUATION_DIR /

        "evaluation_metrics.csv"

    )

    metrics.to_csv(

        metrics_file,

        index=False

    )

    print(f"✓ Saved : {metrics_file}")

    return metrics