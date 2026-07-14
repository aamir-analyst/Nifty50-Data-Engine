import time


def retry(func, retries=5, delay=2):

    for attempt in range(retries):

        try:

            return func()

        except Exception:

            if attempt == retries - 1:

                raise

            time.sleep(delay)