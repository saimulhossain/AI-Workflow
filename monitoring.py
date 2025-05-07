import time
import functools
from app.logger import logger

def monitor_performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.info(f"Function {func.__name__} took {elapsed_time:.4f} seconds")
        with open("logs/performance_metrics.log", "a") as f:
            f.write(f"{time.ctime()}: {func.__name__} took {elapsed_time:.4f} seconds\n")
        return result
    return wrapper