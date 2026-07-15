import joblib
import pandas as pd

from config.config import (
    MODEL_DIR,
    PREDICTION_REPORT,
)
from ml.dataset import DatasetLoader
from ml.target import TargetCreator
from ml.feature_selector import FeatureSelector


class StockPredictor:

    def __init__(self):

        print("=" * 70)
        print("LOADING TRAINED MODEL")
        print("=" * 70)

        self.model = joblib.load(
            MODEL_DIR / "random_forest.pkl"
        )

        self.features = joblib.load(
            MODEL_DIR / "feature_columns.pkl"
        )

        print("✓ Random Forest Loaded")
        print("✓ Feature List Loaded")

    def load_dataset(self):

        loader = DatasetLoader()

        df = loader.prepare()

        target = TargetCreator(df)

        df = target.create()

        selector = FeatureSelector(df)

        X, y, _ = selector.select()

        return df, X
    def predict_latest(self, symbol: str):

        df, X = self.load_dataset()

        print("\n" + "=" * 70)
        print("LATEST STOCK PREDICTION")
        print("=" * 70)

        # ======================================================
        # FILTER STOCK
        # ======================================================

        stock_df = (
            df[df["Symbol"] == symbol]
            .sort_values("Date")
            .reset_index(drop=True)
        )

        if stock_df.empty:
            raise ValueError(f"Stock '{symbol}' not found.")

        # ======================================================
        # LATEST ROW
        # ======================================================

        latest_row = stock_df.iloc[-1]

        latest_index = latest_row.name

        latest_features = X.iloc[[latest_index]]

        prediction = self.model.predict(latest_features)[0]

        print(f"Stock         : {symbol}")
        print(f"Latest Date   : {latest_row['Date']}")
        print(f"Today's Close : {latest_row['Close']:.2f}")
        print(f"Prediction    : {prediction:.2f}")

        return (
            latest_row,
            prediction,
        )
    def analyze_prediction(self, symbol: str):

        (
            latest_row,
            prediction,
        ) = self.predict_latest(symbol)

        print("\n" + "=" * 70)
        print("PREDICTION ANALYSIS")
        print("=" * 70)

        # ======================================================
        # PRICE CHANGE
        # ======================================================

        current_price = latest_row["Close"]

        change = prediction - current_price

        change_percent = (
            change / current_price
        ) * 100

        # ======================================================
        # TRADING SIGNAL
        # ======================================================

        if change_percent >= 2:

            signal = "🟢 STRONG BUY"

        elif change_percent >= 0.5:

            signal = "🟢 BUY"

        elif change_percent <= -2:

            signal = "🔴 STRONG SELL"

        elif change_percent <= -0.5:

            signal = "🔴 SELL"

        else:

            signal = "🟡 HOLD"

        # ======================================================
        # PRINT RESULT
        # ======================================================

        print(f"Current Price      : ₹{current_price:.2f}")

        print(f"Predicted Price    : ₹{prediction:.2f}")

        print(f"Price Difference   : ₹{change:.2f}")

        print(f"Expected Return    : {change_percent:.2f}%")

        print(f"Trading Signal     : {signal}")

        return {
            "symbol": symbol,
            "date": latest_row["Date"],
            "current_price": current_price,
            "predicted_price": prediction,
            "price_difference": change,
            "expected_return": change_percent,
            "signal": signal,
        }
    def scan_market(self):

        df, X = self.load_dataset()

        print("\n" + "=" * 70)
        print("AI MARKET SCANNER")
        print("=" * 70)

        results = []

        # ======================================================
        # LATEST ROW OF EACH STOCK
        # ======================================================

        latest_data = (
            df.sort_values("Date")
              .groupby("Symbol")
              .tail(1)
        )

        # ======================================================
        # PREDICT ALL STOCKS AT ONCE
        # ======================================================

        X_latest = X.loc[latest_data.index]

        predictions = self.model.predict(X_latest)

        # ======================================================
        # CREATE RESULTS
        # ======================================================

        for (_, row), prediction in zip(
            latest_data.iterrows(),
            predictions
        ):

            symbol = row["Symbol"]

            current_price = row["Close"]

            expected_return = (
                (prediction - current_price)
                / current_price
            ) * 100

            if expected_return >= 2:

                signal = "STRONG BUY"

            elif expected_return >= 0.5:

                signal = "BUY"

            elif expected_return <= -2:

                signal = "STRONG SELL"

            elif expected_return <= -0.5:

                signal = "SELL"

            else:

                signal = "HOLD"

            results.append({

                "Symbol": symbol,

                "Current": round(current_price, 2),

                "Prediction": round(prediction, 2),

                "Expected Return %": round(expected_return, 2),

                "Signal": signal

            })

        results = (
            pd.DataFrame(results)
            .sort_values(
                "Expected Return %",
                ascending=False
            )
            .reset_index(drop=True)
        )

        print("\nTOP 10 STOCKS\n")

        print(results.head(10))

        return results
    def save_predictions(self):

        results = self.scan_market()

        print("\n" + "=" * 70)
        print("SAVING PREDICTIONS")
        print("=" * 70)

        # ======================================================
        # SAVE CSV
        # ======================================================

        results.to_csv(
          PREDICTION_REPORT,
            index=False
        )

        print(f"✓ Prediction Report : {PREDICTION_REPORT}")

        # ======================================================
        # TOP BUY
        # ======================================================

        top_buy = (
            results[
                results["Signal"].isin(
                    ["BUY", "STRONG BUY"]
                )
            ]
            .head(5)
        )

        print("\nTOP BUY STOCKS\n")

        print(top_buy)

        # ======================================================
        # TOP SELL
        # ======================================================

        top_sell = (
            results[
                results["Signal"].isin(
                    ["SELL", "STRONG SELL"]
                )
            ]
            .tail(5)
        )

        print("\nTOP SELL STOCKS\n")

        print(top_sell)

        return results
    def run(self):

        print("\n" + "=" * 70)
        print("STARTING AI STOCK PREDICTION")
        print("=" * 70)

        results = self.save_predictions()

        print("\n" + "=" * 70)
        print("PREDICTION COMPLETED")
        print("=" * 70)

        print(f"\nTotal Stocks Scanned : {len(results)}")

        buy = len(
            results[
                results["Signal"].isin(
                    ["BUY", "STRONG BUY"]
                )
            ]
        )

        hold = len(
            results[
                results["Signal"] == "HOLD"
            ]
        )

        sell = len(
            results[
                results["Signal"].isin(
                    ["SELL", "STRONG SELL"]
                )
            ]
        )

        print(f"BUY Signals  : {buy}")

        print(f"HOLD Signals : {hold}")

        print(f"SELL Signals : {sell}")

        print("\nPrediction Report Saved Successfully.")

        return results


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    predictor = StockPredictor()

    predictor.run()