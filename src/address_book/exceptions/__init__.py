# src/address_book/exceptions/__init__.py
"""Package for address book system exceptions.

This package provides custom exception classes used throughout the address book system
for handling various error conditions in a structured way.

Attributes:
    AddressBookException: Base exception for all address book errors.
    ValidationError: Exception for general data validation errors.
    RecordNotFoundException: Exception for when a contact record is not found.
    DuplicateRecordException: Exception for duplicate record entry attempts.
    PhoneError: Base exception for phone-related errors.
    DuplicatePhoneError: Exception for duplicate phone number attempts.
    InvalidPhoneError: Exception for invalid phone number format.
    BirthdayError: Base exception for birthday-related errors.
    InvalidBirthdayError: Exception for invalid birthday format or value.
    DuplicateBirthdayError: Exception for duplicate birthday entry attempts.
    NameError: Base exception for name-related errors.
    EmptyNameError: Exception for empty name values.
    InvalidNameError: Exception for invalid name format.
    PhoneNotFoundException: Exception for non-existent phone number operations.

Example:
    >>> try:
    ...     record.add_phone("123")  # Invalid phone number
    ... except InvalidPhoneError as e:
    ...     print(f"Phone validation failed: {e}")
    ...
    Phone validation failed: Phone number must be exactly 10 digits

Note:
    All custom exceptions inherit from AddressBookException to allow for
    generic error handling when specific error types are not relevant.
"""
from __future__ import annotations

from .exceptions import AddressBookException
from .exceptions import BirthdayError
from .exceptions import DuplicateBirthdayError
from .exceptions import DuplicatePhoneError
from .exceptions import DuplicateRecordException
from .exceptions import EmptyNameError
from .exceptions import InvalidBirthdayError
from .exceptions import InvalidNameError
from .exceptions import InvalidPhoneError
from .exceptions import NameError
from .exceptions import PhoneError
from .exceptions import PhoneNotFoundException
from .exceptions import RecordNotFoundException
from .exceptions import ValidationError

__all__ = [
    'AddressBookException',
    'ValidationError',
    'RecordNotFoundException',
    'PhoneError',
    'DuplicatePhoneError',
    'InvalidPhoneError',
    'BirthdayError',
    'InvalidBirthdayError',
    'NameError',
    'EmptyNameError',
    'InvalidNameError',
    'PhoneNotFoundException',
    'DuplicateBirthdayError',
    'DuplicateRecordException',
]
