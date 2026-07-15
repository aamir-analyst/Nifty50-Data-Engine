import pandas as pd


class PerformanceMetrics:

    def __init__(self, portfolio: pd.DataFrame):

        self.portfolio = portfolio

    def calculate(self):

        total_investment = self.portfolio["Investment"].sum()

        final_value = self.portfolio["Final Value"].sum()

        total_profit = self.portfolio["Profit"].sum()

        total_return = (
            total_profit / total_investment
        ) * 100

        winning = len(
            self.portfolio[
                self.portfolio["Profit"] > 0
            ]
        )

        losing = len(
            self.portfolio[
                self.portfolio["Profit"] < 0
            ]
        )

        hold = len(
            self.portfolio[
                self.portfolio["Signal"] == "HOLD"
            ]
        )

        win_rate = (
            winning / len(self.portfolio)
        ) * 100

        print("\n" + "=" * 70)
        print("BACKTEST PERFORMANCE")
        print("=" * 70)

        print(f"Initial Capital : ₹ {total_investment:,.2f}")

        print(f"Final Value     : ₹ {final_value:,.2f}")

        print(f"Profit          : ₹ {total_profit:,.2f}")

        print(f"Return          : {total_return:.2f}%")

        print(f"Winning Trades  : {winning}")

        print(f"Losing Trades   : {losing}")

        print(f"Hold Signals    : {hold}")

        print(f"Win Rate        : {win_rate:.2f}%")

        return {

            "Investment": total_investment,

            "Final": final_value,

            "Profit": total_profit,

            "Return": total_return,

            "Win Rate": win_rate

        }