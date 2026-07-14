from datetime import date, timedelta


def generate_dates(start_year=2000, end_year=2026):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)

    current = start

    while current <= end:

        # Monday-Friday
        if current.weekday() < 5:
            yield current

        current += timedelta(days=1)