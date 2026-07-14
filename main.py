import argparse
import sys

from scraper.downloader import StockDownloader
from scraper.merger import DataMerger
from scraper.validator import DataValidator

from database_manager.sqlite_manager import SQLiteManager
from features.pipeline import FeaturePipeline

from utils.logger import pipeline_logger as logger


def banner():
    print("=" * 70)
    print("📈 NIFTY50 DATA ENGINE v2.3")
    print("=" * 70)


def download():
    logger.info("Downloading stock data...")
    StockDownloader().run()


def merge():
    logger.info("Merging stock files...")
    DataMerger().merge()


def database():
    logger.info("Creating SQLite database...")

    db = SQLiteManager()
    db.create_database()

    print("\nDatabase Preview\n")
    print(
        db.query(
            """
            SELECT *
            FROM stocks
            LIMIT 10
            """
        )
    )

    db.close()


def validate():
    logger.info("Validating dataset...")
    DataValidator().run()


def features():
    logger.info("Generating technical indicators...")
    FeaturePipeline().run()


def reports():

    import pandas as pd

    from config.config import PROCESSED_DIR
    from reports.report_generator import ReportGenerator

    print("=" * 70)
    print("REPORT GENERATION")
    print("=" * 70)

    df = pd.read_csv(
        PROCESSED_DIR / "features.csv"
    )

    report = ReportGenerator()

    report.validation_report(df)

    report.feature_report(df)

    print("\n✅ All Reports Generated Successfully")
def run_all():

    banner()

    download()

    merge()

    database()

    validate()

    features()

    reports()

    print("\n" + "=" * 70)
    print("🎉 COMPLETE DATA PIPELINE FINISHED")
    print("=" * 70)

    logger.info("Pipeline completed successfully.")


def main():

    parser = argparse.ArgumentParser(
        description="Nifty50 Data Engine"
    )

    parser.add_argument("--all", action="store_true")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--merge", action="store_true")
    parser.add_argument("--database", action="store_true")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--features", action="store_true")
    parser.add_argument("--report", action="store_true")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    if args.all:
        run_all()

    if args.download:
        download()

    if args.merge:
        merge()

    if args.database:
        database()

    if args.validate:
        validate()

    if args.features:
        features()

    if args.report:
        reports()


if __name__ == "__main__":
    main()