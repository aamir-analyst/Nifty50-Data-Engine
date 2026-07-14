import pandas as pd

from ta.volatility import (
    BollingerBands,
    AverageTrueRange,
)


class VolatilityEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate(self):

        print("=" * 70)
        print("CALCULATING VOLATILITY INDICATORS")
        print("=" * 70)

        result = []

        for symbol, stock in self.df.groupby("Symbol"):

            stock = stock.sort_values("Date").copy()

            close = stock["Close"]
            high = stock["High"]
            low = stock["Low"]

            # ---------------------------------
            # Bollinger Bands
            # ---------------------------------

            bb = BollingerBands(
                close=close,
                window=20,
                window_dev=2
            )

            stock["BB_UPPER"] = bb.bollinger_hband()
            stock["BB_MIDDLE"] = bb.bollinger_mavg()
            stock["BB_LOWER"] = bb.bollinger_lband()

            # ---------------------------------
            # ATR
            # ---------------------------------

            atr = AverageTrueRange(
                high=high,
                low=low,
                close=close,
                window=14
            )

            stock["ATR_14"] = atr.average_true_range()

            result.append(stock)

            print(f"✅ {symbol}")

        df = pd.concat(result, ignore_index=True)

        print("=" * 70)
        print("VOLATILITY COMPLETED")
        print("=" * 70)

        return df