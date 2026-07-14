import argparse

from scraper.downloader import StockDownloader
from scraper.merger import DataMerger
from scraper.validator import DataValidator

from database_manager.sqlite_manager import SQLiteManager

from features.pipeline import FeaturePipeline


# ==========================================================
# DOWNLOAD
# ==========================================================

def run_download():

    downloader = StockDownloader()
    downloader.run()


# ==========================================================
# MERGE
# ==========================================================

def run_merge():

    merger = DataMerger()
    merger.merge()


# ==========================================================
# DATABASE
# ==========================================================

def run_database():

    db = SQLiteManager()

    db.create_database()

    print("\n✅ Database Ready!")

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


# ==========================================================
# VALIDATION
# ==========================================================

def run_validation():

    validator = DataValidator()

    validator.run()


# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

def run_features():

    pipeline = FeaturePipeline()

    feature_df = pipeline.run()

    print("\nFeature Preview\n")

    print(feature_df.head(10))


# ==========================================================
# COMPLETE PIPELINE
# ==========================================================

def run_all():

    print("=" * 70)
    print("NIFTY50 DATA ENGINE")
    print("=" * 70)

    run_download()

    run_merge()

    run_database()

    run_validation()

    run_features()

    print("\n" + "=" * 70)
    print("🎉 COMPLETE DATA PIPELINE FINISHED")
    print("=" * 70)


# ==========================================================
# CLI
# ==========================================================

def main():

    parser = argparse.ArgumentParser(
        description="Nifty50 Data Engine"
    )

    parser.add_argument(
        "--download",
        action="store_true",
        help="Download Stock Data"
    )

    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge Stock CSV Files"
    )

    parser.add_argument(
        "--database",
        action="store_true",
        help="Create SQLite Database"
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate Dataset"
    )

    parser.add_argument(
        "--features",
        action="store_true",
        help="Generate Technical Indicators"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run Complete Pipeline"
    )

    args = parser.parse_args()

    if args.download:
        run_download()

    elif args.merge:
        run_merge()

    elif args.database:
        run_database()

    elif args.validate:
        run_validation()

    elif args.features:
        run_features()

    elif args.all:
        run_all()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()