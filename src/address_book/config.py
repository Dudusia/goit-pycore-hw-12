from pathlib import Path
from logging import INFO

class Config:
    # General
    CURRENT_DIR = Path(__file__).parent

    # Storage
    STORAGE_DIR = CURRENT_DIR / "storage"
    STORAGE_DIR.mkdir(exist_ok=True)
    STORAGE_FILE_NAME = "addressbook.pkl"
    STORAGE_FILE_PATH = (STORAGE_DIR / STORAGE_FILE_NAME).absolute()

    # Logs
    LOG_LEVEL = INFO
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_FILEMODE = "w"
    LOG_DIR = CURRENT_DIR / "logs"
    LOG_DIR.mkdir(exist_ok=True)
    LOG_FILE_NAME = "log.log"
    LOG_FILE_PATH = (CURRENT_DIR / LOG_DIR / LOG_FILE_NAME).absolute()


