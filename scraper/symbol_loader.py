from pathlib import Path
from playwright.sync_api import sync_playwright
import pandas as pd


class SymbolLoader:

    def __init__(self):
        self.output = Path("data/current_symbols.csv")

    def download(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)

            page = browser.new_page()

            page.goto(
                "https://www.nseindia.com/static/products-services/indices-nifty50-index",
                wait_until="networkidle"
            )

            with page.expect_download() as download_info:

                page.get_by_text("List of Nifty 50 stocks").click()

            download = download_info.value

            download.save_as(self.output)

            browser.close()

        print("Downloaded :", self.output)

    def load(self):

        if not self.output.exists():
            self.download()

        df = pd.read_csv(self.output)

        return df