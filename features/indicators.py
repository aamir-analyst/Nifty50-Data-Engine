import pandas as pd

from ta.trend import (
    SMAIndicator,
    EMAIndicator,
    MACD,
)

from ta.momentum import RSIIndicator


class IndicatorEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate(self):

        print("=" * 70)
        print("CALCULATING INDICATORS")
        print("=" * 70)

        result = []

        for symbol, stock in self.df.groupby("Symbol"):

            stock = stock.sort_values("Date").copy()

            close = stock["Close"]

            # ------------------------
            # SMA
            # ------------------------

            stock["SMA_20"] = SMAIndicator(
                close,
                window=20
            ).sma_indicator()

            stock["SMA_50"] = SMAIndicator(
                close,
                window=50
            ).sma_indicator()

            stock["SMA_100"] = SMAIndicator(
                close,
                window=100
            ).sma_indicator()

            stock["SMA_200"] = SMAIndicator(
                close,
                window=200
            ).sma_indicator()

            # ------------------------
            # EMA
            # ------------------------

            stock["EMA_20"] = EMAIndicator(
                close,
                window=20
            ).ema_indicator()

            stock["EMA_50"] = EMAIndicator(
                close,
                window=50
            ).ema_indicator()

            stock["EMA_200"] = EMAIndicator(
                close,
                window=200
            ).ema_indicator()

            # ------------------------
            # RSI
            # ------------------------

            stock["RSI_14"] = RSIIndicator(
                close,
                window=14
            ).rsi()

            # ------------------------
            # MACD
            # ------------------------

            macd = MACD(close)

            stock["MACD"] = macd.macd()
            stock["MACD_SIGNAL"] = macd.macd_signal()
            stock["MACD_HIST"] = macd.macd_diff()

            result.append(stock)

            print(f"✅ {symbol}")

        df = pd.concat(result)

        print("=" * 70)
        print("INDICATORS COMPLETED")
        print("=" * 70)

        return df