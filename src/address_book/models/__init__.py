# src/address_book/models/__init__.py
"""Models package for the address book system.

This package provides the core data models and storage functionality for the
address book system. It includes classes for managing contacts, their fields,
and the address book itself.

Classes:
    Field: Base field class for contact attributes.
        A common ancestor for all field types that provides basic validation
        and value storage functionality.

    Name: Field implementation for contact names.
        Validates and stores contact names, ensuring they meet format requirements
        and contain valid characters.

    Phone: Field implementation for phone numbers.
        Handles phone number validation and storage, ensuring numbers contain
        exactly 10 digits.

    Birthday: Field implementation for birth dates.
        Manages birthday dates, ensuring valid format (DD.MM.YYYY) and preventing
        future dates.

    Record: Container for contact information.
        Manages a single contact's data including name, multiple phone numbers,
        and birthday information.

    AddressBook: Main container for all contacts.
        Manages the collection of all contacts and provides methods for adding,
        finding, and managing records.

Example:
    Basic usage of the address book system:

    >>> from models import AddressBook, Record
    >>>
    >>> # Create a new address book
    >>> book = AddressBook()
    >>>
    >>> # Create and add a new contact
    >>> record = Record("John")
    >>> record.add_phone("1234567890")
    >>> record.add_birthday("01.01.1990")
    >>> book.add_record(record)

Field Validation:
    Each field type implements specific validation rules:
    - Names: Must be non-empty strings with valid characters
    - Phones: Must be exactly 10 digits
    - Birthdays: Must be in DD.MM.YYYY format and not in the future

Notes:
    - The Record class allows multiple phone numbers per contact
    - Birthday dates are validated to prevent future dates
    - All fields raise appropriate exceptions for invalid data
    - The AddressBook class inherits from UserDict for dict-like behavior
"""
from __future__ import annotations

from .field import Field
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .record import Record
from .address_book import AddressBook

__all__ = ["Field", "Name", "Phone", "Record", "AddressBook", "Birthday"]
