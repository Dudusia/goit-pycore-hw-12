# src/address_book/main.py
"""Main module for the Address Book application.

This module provides the entry point and core functionality for the address book
system. It handles data persistence and initializes the command-line interface.

"""
from __future__ import annotations

import pickle

from config import Config
from interface import CLIHandler
from models import AddressBook


def save_data(book, filename=Config.STORAGE_FILE_PATH):
    """Save address book data to file.

    Args:
        book: AddressBook instance to save.
        filename: Path to save the data. Defaults to Config.STORAGE_FILE_PATH.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=Config.STORAGE_FILE_PATH):
    """Load address book data from file.

    Args:
        filename: Path to load the data from. Defaults to Config.STORAGE_FILE_PATH.

    Returns:
        AddressBook: Loaded address book or new instance if file not found.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    """Run the address book application.

    Loads saved data, initializes the CLI interface, and handles data persistence.
    """
    book = load_data()
    cli = CLIHandler(book)

    try:
        cli.run()
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
