# src/address_book/models/__init__.py
"""Address Book Package.

This package provides a complete implementation of an address book system with
support for managing contacts, their phone numbers, and birthdays.

Classes:
    Field: Abstract base class for all field types in the address book.
    Name: Field subclass for storing and validating contact names.
    Phone: Field subclass for storing and validating phone numbers.
    Birthday: Field subclass for storing and validating birth dates.
    Record: Container class for managing individual contacts and their fields.
    AddressBook: Main class for storing and managing all contact records.

Usage Example:
    from models import AddressBook, Record

    # Create a new address book
    book = AddressBook()

    # Add a new contact
    record = Record("John")
    record.add_phone("1234567890")
    record.add_birthday("01.01.1990")
    book.add_record(record)

All fields implement validation to ensure data integrity:
- Names cannot be empty
- Phone numbers must be exactly 10 digits
- Birthdays must be in DD.MM.YYYY format and not in the future

The package handles common operations like:
- Adding/removing contacts
- Managing multiple phone numbers per contact
- Tracking birthdays
- Generating upcoming birthday notifications
"""
from __future__ import annotations

from .field import Field
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .record import Record
from .address_book import AddressBook

__all__ = ["Field", "Name", "Phone", "Record", "AddressBook", "Birthday"]
