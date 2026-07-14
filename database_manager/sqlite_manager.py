import sqlite3
import pandas as pd

from config.config import DATABASE_FILE
from config.config import MERGED_DIR


class SQLiteManager:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE_FILE)

    def create_database(self):

        csv_file = MERGED_DIR / "all_stocks.csv"

        df = pd.read_csv(csv_file)

        df.to_sql(
            "stocks",
            self.conn,
            if_exists="replace",
            index=False,
        )

        print("=" * 60)
        print("DATABASE CREATED")
        print("=" * 60)
        print(f"Rows : {len(df):,}")

    def query(self, sql):

        return pd.read_sql(sql, self.conn)

    def close(self):

        self.conn.close()