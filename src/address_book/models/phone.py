# src/address_book/models/phone.py
"""Module containing the Phone field class.

This module provides the Phone class for storing and validating phone numbers
in the address book system.
"""
from __future__ import annotations

from typing import Any

from exceptions import InvalidPhoneError
from models import Field


class Phone(Field):
    """Class representing a phone number.

    Extends the Field class with specific validation for phone numbers.
    Phone numbers must be exactly 10 digits.

    Attributes:
        _value (str): Protected storage for the phone number.
    """

    @property
    def value(self) -> str:
        """Get the stored phone number.

        Returns:
            str: The stored phone number.
        """
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Set the phone number with validation.

        Args:
            new_value: The new phone number to store.

        Raises:
            InvalidPhoneError: If the phone number is not exactly 10 digits or not a string.
        """
        if not isinstance(new_value, str):
            raise InvalidPhoneError("Phone number must be a string")

        # Remove any spaces or common separators
        cleaned_value = ''.join(filter(str.isdigit, new_value))

        if not cleaned_value.isdigit():
            raise InvalidPhoneError("Phone number must contain only digits")

        if len(cleaned_value) != 10:
            raise InvalidPhoneError("Phone number must be exactly 10 digits")

        self._value = cleaned_value
