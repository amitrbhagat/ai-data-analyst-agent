import logging 
import os
from datetime import date


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger('ai_data_analyst')
logger.setLevel(logging.INFO)


if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def log_step(request_id:str, step_name:str, duration_ms:float, status:str, extra:dict|None=None):    

    message = (
        f"[{request_id}] "
        f"{step_name} | "
        f"{duration_ms / 1000:.2f}s | "
        f"{status}"
    )

    if extra:
        extra_text = "|".join(
            f"{key}={value}"
            for key, value in extra.items()
        )
        message += f" | {extra_text}"


    logger.info(message)    
