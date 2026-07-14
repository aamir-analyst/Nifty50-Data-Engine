import numpy as np
import pandas as pd


class ReturnsEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate(self):

        print("=" * 70)
        print("CALCULATING RETURNS")
        print("=" * 70)

        result = []

        for symbol, stock in self.df.groupby("Symbol"):

            stock = stock.sort_values("Date").copy()

            # -----------------------------
            # Daily Return
            # -----------------------------

            stock["DAILY_RETURN"] = stock["Close"].pct_change(fill_method=None)

            # -----------------------------
            # Log Return
            # -----------------------------

            stock["LOG_RETURN"] = np.log(
                stock["Close"] /
                stock["Close"].shift(1)
            )

            # -----------------------------
            # Cumulative Return
            # -----------------------------

            stock["CUMULATIVE_RETURN"] = (
                (1 + stock["DAILY_RETURN"])
                .cumprod() - 1
            )

            result.append(stock)

            print(f"✅ {symbol}")

        df = pd.concat(result, ignore_index=True)

        print("=" * 70)
        print("RETURNS COMPLETED")
        print("=" * 70)

        return df