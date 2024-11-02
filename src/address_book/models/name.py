# src/address_book/models/name.py
"""Module containing the Name field class.

This module provides the Name class for storing and validating contact names
in the address book system.
"""
from __future__ import annotations

import re
from typing import Any

from exceptions import EmptyNameError
from exceptions import InvalidNameError
from models import Field


class Name(Field):
    """Class representing a contact's name.

    Extends the Field class with specific validation for name values.
    Names must be non-empty strings and contain valid characters.

    Attributes:
        _value (str): Protected storage for the name value.
    """

    @property
    def value(self) -> str:
        """Get the stored name value.

        Returns:
            str: The stored name.
        """
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Set the name value with validation.

        Args:
            new_value: The new name to store.

        Raises:
            EmptyNameError: If the name is empty.
            InvalidNameError: If the name is not a string or not a proper name.
        """
        if not isinstance(new_value, str):
            raise InvalidNameError("Name must be a string")
        if not re.match(r'^[a-zA-Z](?:[a-zA-Z0-9]|(?<![ -])[ -](?![ -])){1,}$', new_value):
            raise InvalidNameError("Value provided should be a proper name.")
        if not new_value.strip():
            raise EmptyNameError("Name cannot be empty")
        self._value = new_value.strip()
