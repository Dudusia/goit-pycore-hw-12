# src/address_book/models/phone.py
"""Phone field implementation for the address book system.

This module provides the Phone class for storing and validating phone numbers.
It ensures phone numbers contain exactly 10 digits and handles various input formats.

Note:
    Valid phone numbers must:
    - Contain exactly 10 digits
    - Contain only numeric characters (spaces and common separators are stripped)
"""
from __future__ import annotations

from typing import Any

from exceptions import InvalidPhoneError
from models import Field


class Phone(Field):
    """Field implementation for storing and validating phone numbers.

    The Phone class ensures that phone numbers contain exactly 10 digits. It
    automatically cleans input by removing spaces and common separators.

    Args:
        value: The phone number string to validate and store.

    Raises:
        InvalidPhoneError: If the phone number is invalid (wrong length or non-digits).

    Attributes:
        _value: Protected storage for the cleaned phone number string.
    """

    @property
    def value(self) -> str:
        """Get the stored phone number.

        Returns:
            str: The cleaned phone number (10 digits only).
        """
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Set and validate the phone number.

        Cleans and validates the phone number by removing spaces and separators,
        then ensuring exactly 10 digits remain.

        Args:
            new_value: The new phone number to validate and store.

        Raises:
            InvalidPhoneError: If any of these conditions are met:
                - Input is not a string
                - Cleaned number contains non-digit characters
                - Cleaned number is not exactly 10 digits

        Note:
            Common phone number formats that are automatically cleaned:
            - Spaces: "123 456 7890"
            - Hyphens: "123-456-7890"
            - Parentheses: "(123) 456 7890"
            All must result in exactly 10 digits after cleaning.
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
