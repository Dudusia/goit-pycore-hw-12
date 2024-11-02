# src/address_book/exceptions/__init__.py
"""Exceptions package for the address book system.

This package provides all custom exceptions used throughout the address book system.
Import all exceptions here to provide a clean interface for other modules.
"""
from __future__ import annotations

from .exceptions import AddressBookException
from .exceptions import BirthdayError
from .exceptions import DuplicateBirthdayError
from .exceptions import DuplicatePhoneError
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
    'InvalidBirthdayError'
    'NameError',
    'EmptyNameError',
    'InvalidNameError',
    'PhoneNotFoundException',
    'DuplicateBirthdayError',
]
