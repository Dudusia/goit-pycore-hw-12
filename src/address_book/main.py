# src/address_book/main.py
"""Main module for the Address Book application."""
from __future__ import annotations

import pickle

from config import Config
from models import AddressBook
from interface.cli_handler import CLIHandler

def save_data(book, filename=Config.STORAGE_FILE_PATH):
    """Save address book data to file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename=Config.STORAGE_FILE_PATH):
    """Load address book data from file."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    """Main function that runs the address book application."""
    book = load_data()
    cli = CLIHandler(book)

    try:
        cli.run()
    finally:
        save_data(book)

if __name__ == "__main__":
    main()
