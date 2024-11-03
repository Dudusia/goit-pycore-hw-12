# src/address_book/__init__.py
"""Address book management system package.

This is the top-level package of the address book system. It provides access
to configuration settings used throughout the application.

Example:
    >>> from address_book import Config
    >>> print(Config.STORAGE_DIR)  # Access storage directory path
"""
from __future__ import annotations

from .config import Config

__all__ = ["Config"]
