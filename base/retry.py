import logging
import time

def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logging.info(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            logging.info(f"Function failed after {max_attempts} attempts")
        return wrapper
    return decorator