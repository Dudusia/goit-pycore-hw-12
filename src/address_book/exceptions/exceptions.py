# src/address_book/exceptions/exceptions.py
"""Custom exceptions for the address book system."""
from __future__ import annotations


class AddressBookException(Exception):
    """Base exception class for AddressBook errors."""
    pass


class ValidationError(AddressBookException):
    """Raised when input data fails validation."""
    pass


class RecordNotFoundException(AddressBookException):
    """Raised when a record is not found in the address book."""
    pass

# Phone-related exceptions


class PhoneError(ValidationError):
    """Base exception class for phone-related errors."""
    pass


class DuplicatePhoneError(PhoneError):
    """Raised when attempting to add a duplicate phone number."""
    pass


class InvalidPhoneError(PhoneError):
    """Raised when a phone number is invalid."""
    pass


class PhoneNotFoundException(PhoneError):
    """Raised when attempting to remove the non-existing phone number."""
    pass

# Birthday-related exceptions


class BirthdayError(ValidationError):
    """Raised for birthday-related errors."""
    pass


class InvalidBirthdayError(BirthdayError):
    """Raised when birthday is provided in invalid format or is invalid itself"""
    pass


class DuplicateBirthdayError(BirthdayError):
    """Raised when attempting to add a birthday to a contact that already has one."""
    pass

# Name-related exceptions


class NameError(ValidationError):
    """Base exception class for name-related errors."""
    pass


class EmptyNameError(NameError):
    """Raised when attempting to set an empty name."""
    pass


class InvalidNameError(NameError):
    """Raised when name contains invalid characters or format."""
    pass
