import pandas as pd
from backtesting.metrics import PerformanceMetrics
from config.config import REPORT_DIR
from backtesting.strategy import get_signal


class BacktestEngine:

    def __init__(self, initial_capital=100000):

        self.initial_capital = initial_capital

        self.cash = initial_capital

        self.position = 0

        self.trade_history = []

    def load_predictions(self):

        file = REPORT_DIR / "market_predictions.csv"

        if not file.exists():
            raise FileNotFoundError(
                "Run: python main.py --predict"
            )

        return pd.read_csv(file)

    def run(self):

        print("=" * 70)
        print("BACKTEST STARTED")
        print("=" * 70)

        df = self.load_predictions()

        portfolio = []

        for _, row in df.iterrows():

            signal = get_signal(
                row["Expected Return %"]
            )

            current = row["Current"]

            prediction = row["Prediction"]

            expected = row["Expected Return %"]

            investment = self.initial_capital / len(df)

            future_value = investment * (
                1 + expected / 100
            )

            profit = future_value - investment

            portfolio.append({

                "Symbol": row["Symbol"],

                "Signal": signal,

                "Investment": round(investment, 2),

                "Expected Return %": round(expected, 2),

                "Profit": round(profit, 2),

                "Final Value": round(future_value, 2)

            })

        result = pd.DataFrame(portfolio)


        print(result.head())

        metrics = PerformanceMetrics(result)

        metrics.calculate()

        return result
    
if __name__ == "__main__":

    engine = BacktestEngine()

    result = engine.run()

    print("\nPortfolio Shape")

    print(result.shape)