# src/address_book/config.py
"""Configuration settings for the address book system.

This module defines application-wide configuration settings including paths
for storage, logs, and other system parameters.

Attributes:
    CURRENT_DIR: Path to the current directory.
    STORAGE_DIR: Directory for persistent data storage.
    STORAGE_FILE_NAME: Name of the address book data file.
    STORAGE_FILE_PATH: Full path to the address book data file.
    STORAGE_CLI_HISTORY_FILENAME: Name of CLI history file.
    STORAGE_CLI_HISTORY_FILE_PATH: Full path to CLI history file.
    LOG_LEVEL: Logging level (default: INFO).
    LOG_FORMAT: Format string for log messages.
    LOG_FILEMODE: File mode for log file ('w' for write).
    LOG_DIR: Directory for log files.
    LOG_FILE_NAME: Name of the log file.
    LOG_FILE_PATH: Full path to the log file.
"""
from __future__ import annotations

from logging import INFO
from pathlib import Path


class Config:
    """Configuration settings container.

    This class provides centralized access to all configuration settings
    used throughout the address book system.

    Note:
        All paths are created automatically if they don't exist.
    """
    # General
    CURRENT_DIR = Path(__file__).parent

    # Storage
    STORAGE_DIR = CURRENT_DIR / "storage"
    STORAGE_DIR.mkdir(exist_ok=True)
    STORAGE_FILE_NAME = "addressbook.pkl"
    STORAGE_FILE_PATH = (STORAGE_DIR / STORAGE_FILE_NAME).absolute()
    STORAGE_CLI_HISTORY_FILENAME = ".address_book_history"
    STORAGE_CLI_HISTORY_FILE_PATH = (STORAGE_DIR / STORAGE_CLI_HISTORY_FILENAME).absolute()

    # Logs
    LOG_LEVEL = INFO
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_FILEMODE = "w"
    LOG_DIR = CURRENT_DIR / "logs"
    LOG_DIR.mkdir(exist_ok=True)
    LOG_FILE_NAME = "log.log"
    LOG_FILE_PATH = (CURRENT_DIR / LOG_DIR / LOG_FILE_NAME).absolute()
