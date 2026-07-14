from pathlib import Path
import pandas as pd
import yfinance as yf
from tqdm import tqdm

from config.config import (
    RAW_STOCK_DIR,
    START_DATE,
    END_DATE,
    SYMBOL_FILE,
)

from utils.helpers import read_symbols
from utils.logger import download_logger as logger


class StockDownloader:

    def __init__(self):
        self.symbols = read_symbols(SYMBOL_FILE)

    def download_stock(self, symbol: str):

        output_file = RAW_STOCK_DIR / f"{symbol}.csv"

        # Skip only if file is valid
        if output_file.exists():
            try:
                test = pd.read_csv(output_file)

                required = [
                    "Date",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Adj Close",
                    "Volume",
                    "Symbol",
                ]

                if all(col in test.columns for col in required):
                    print(f"✅ Skipped : {symbol}")
                    return

                print(f"⚠ Invalid File Found. Re-downloading : {symbol}")

            except Exception:
                print(f"⚠ Corrupted File. Re-downloading : {symbol}")

        try:

            print(f"⬇ Downloading : {symbol}")

            df = yf.download(
                tickers=symbol,
                start=START_DATE,
                end=END_DATE,
                auto_adjust=False,
                actions=False,
                progress=False,
                group_by="column",
                threads=False,
            )

            if df.empty:
                logger.warning(f"No data found : {symbol}")
                print(f"❌ No Data : {symbol}")
                return

            # Convert Date index into column
            df = df.reset_index()

            # Handle MultiIndex (latest yfinance)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            # Ensure Date column
            if df.columns[0] != "Date":
                df.rename(columns={df.columns[0]: "Date"}, inplace=True)

            # Add Symbol
            df["Symbol"] = symbol

            expected_columns = [
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Adj Close",
                "Volume",
                "Symbol",
            ]

            missing = [c for c in expected_columns if c not in df.columns]

            if missing:
                raise ValueError(f"Missing Columns : {missing}")

            df = df[expected_columns]

            df.to_csv(output_file, index=False)

            logger.info(f"{symbol} downloaded successfully")

            print(f"✅ Saved : {symbol}")

        except Exception as e:

            logger.error(f"{symbol} : {e}")

            print(f"❌ Error downloading {symbol}")
            print(e)

    def run(self):

        print("=" * 60)
        print("NIFTY50 DATA DOWNLOADER")
        print("=" * 60)

        print(f"Downloading {len(self.symbols)} stocks...\n")

        for symbol in tqdm(self.symbols, ncols=100):

            self.download_stock(symbol)

        print("\n🎉 Download Completed.")