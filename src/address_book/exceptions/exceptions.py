# src/address_book/exceptions/exceptions.py
"""Custom exceptions for the address book system.

This module defines the exception hierarchy used throughout the address book system
to handle various error conditions in a structured way.

Exception Hierarchy:
    AddressBookException
    ├── ValidationError
    │   ├── PhoneError
    │   │   ├── DuplicatePhoneError
    │   │   ├── InvalidPhoneError
    │   │   └── PhoneNotFoundException
    │   ├── BirthdayError
    │   │   ├── InvalidBirthdayError
    │   │   └── DuplicateBirthdayError
    │   └── NameError
    │       ├── EmptyNameError
    │       └── InvalidNameError
    └── RecordNotFoundException
"""
from __future__ import annotations


class AddressBookException(Exception):
    """Base exception class for the address book system.

    All custom exceptions in the address book system inherit from this class,
    allowing for catch-all error handling when specific error types are not relevant.

    Example:
        >>> try:
        ...     raise AddressBookException("Custom error message")
        ... except AddressBookException as e:
        ...     print(e)
        Custom error message
    """
    pass


class ValidationError(AddressBookException):
    """Base exception for data validation errors.

    Used when input data fails validation rules. Serves as a parent class
    for more specific validation error types.

    Example:
        >>> try:
        ...     raise ValidationError("Invalid data format")
        ... except ValidationError as e:
        ...     print(e)
        Invalid data format
    """
    pass


class RecordNotFoundException(AddressBookException):
    """Exception raised when a requested contact record is not found.

    Raised when attempting to access, modify, or delete a non-existent contact.

    Example:
        >>> try:
        ...     raise RecordNotFoundException("Contact 'John' not found")
        ... except RecordNotFoundException as e:
        ...     print(e)
        Contact 'John' not found
    """
    pass


class DuplicateRecordException(AddressBookException):
    """Exception raised when attempting to add contact record that already exist.

    Raised when trying to add a record that already exists in the address book.

    Example:
        >>> try:
        ...     raise DuplicateRecordException("Contact 'John' already exist")
        ... except DuplicateRecordException as e:
        ...     print(e)
        Contact 'John' already exist
    """
    pass


class PhoneError(ValidationError):
    """Base exception for phone number-related errors.

    Parent class for all phone number validation and operation errors.
    """
    pass


class DuplicatePhoneError(PhoneError):
    """Exception raised when attempting to add a duplicate phone number.

    Raised when trying to add a phone number that already exists for a contact.

    Example:
        >>> try:
        ...     raise DuplicatePhoneError("Phone number already exists")
        ... except DuplicatePhoneError as e:
        ...     print(e)
        Phone number already exists
    """
    pass


class InvalidPhoneError(PhoneError):
    """Exception raised when a phone number is invalid.

    Raised when a phone number doesn't meet the required format (exactly 10 digits)
    or contains invalid characters.

    Example:
        >>> try:
        ...     raise InvalidPhoneError("Phone must be exactly 10 digits")
        ... except InvalidPhoneError as e:
        ...     print(e)
        Phone must be exactly 10 digits
    """
    pass


class PhoneNotFoundException(PhoneError):
    """Exception raised when attempting to modify a non-existent phone number.

    Raised when trying to edit or remove a phone number that doesn't exist
    for the specified contact.

    Example:
        >>> try:
        ...     raise PhoneNotFoundException("Phone number not found")
        ... except PhoneNotFoundException as e:
        ...     print(e)
        Phone number not found
    """
    pass


class BirthdayError(ValidationError):
    """Base exception for birthday-related errors.

    Parent class for all birthday validation and operation errors.
    """
    pass


class InvalidBirthdayError(BirthdayError):
    """Exception raised when a birthday date is invalid.

    Raised when a birthday date is in an invalid format, is a future date,
    or contains invalid values.

    Example:
        >>> try:
        ...     raise InvalidBirthdayError("Invalid date format")
        ... except InvalidBirthdayError as e:
        ...     print(e)
        Invalid date format
    """
    pass


class DuplicateBirthdayError(BirthdayError):
    """Exception raised when attempting to add a birthday to a contact that already has one.

    Raised when trying to add a birthday to a contact that already has a birthday set.

    Example:
        >>> try:
        ...     raise DuplicateBirthdayError("Birthday already exists")
        ... except DuplicateBirthdayError as e:
        ...     print(e)
        Birthday already exists
    """
    pass


class NameError(ValidationError):
    """Base exception for name-related errors.

    Parent class for all name validation and operation errors.
    """
    pass


class EmptyNameError(NameError):
    """Exception raised when attempting to set an empty name.

    Raised when trying to create or update a contact with an empty name
    or whitespace-only name.

    Example:
        >>> try:
        ...     raise EmptyNameError("Name cannot be empty")
        ... except EmptyNameError as e:
        ...     print(e)
        Name cannot be empty
    """
    pass


class InvalidNameError(NameError):
    """Exception raised when a name contains invalid characters or format.

    Raised when a name contains invalid characters, starts with non-letter
    characters, or doesn't follow the required format.

    Example:
        >>> try:
        ...     raise InvalidNameError("Name contains invalid characters")
        ... except InvalidNameError as e:
        ...     print(e)
        Name contains invalid characters
    """
    pass
