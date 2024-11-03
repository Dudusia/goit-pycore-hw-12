# src/address_book/models/name.py
"""Name field implementation for the address book system.

This module provides the Name class for storing and validating contact names.
It ensures names contain only valid characters and follow proper formatting rules.

Note:
    Valid names must:
    - Start with a letter
    - Contain only letters, numbers, spaces, and hyphens
    - Not have consecutive spaces or hyphens
    - Not be empty or whitespace-only
"""
from __future__ import annotations

import re
from typing import Any

from exceptions import EmptyNameError
from exceptions import InvalidNameError
from models import Field


class Name(Field):
    """Field implementation for storing and validating contact names.

    The Name class ensures that contact names are properly formatted and contain
    only valid characters. It enforces various rules to maintain data quality.

    Args:
        value: The name string to validate and store.

    Raises:
        EmptyNameError: If the name is empty or contains only whitespace.
        InvalidNameError: If the name contains invalid characters or format.

    Attributes:
        _value: Protected storage for the name string.
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
        """Set and validate the name value.

        Args:
            new_value: The new name to validate and store.

        Raises:
            InvalidNameError: If any of these conditions are met:
                - Input is not a string
                - Name doesn't start with a letter
                - Name contains invalid characters
                - Name has consecutive spaces or hyphens
            EmptyNameError: If the name is empty or whitespace-only

        Note:
            The name validation regex ensures:
            - First character is a letter
            - Only letters, numbers, spaces, and hyphens are allowed
            - No consecutive spaces or hyphens
            - At least one character after any space or hyphen
        """
        if not isinstance(new_value, str):
            raise InvalidNameError("Name must be a string")

        if not new_value.strip():
            raise EmptyNameError("Name cannot be empty")

        # Regex pattern explanation:
        # ^[a-zA-Z] - starts with a letter
        # (?:[a-zA-Z0-9]|(?<![ -])[ -](?![ -])){1,}$ - followed by:
        #   - letters or numbers
        #   - single spaces or hyphens (not at start/end, not consecutive)
        if not re.match(r'^[a-zA-Z](?:[a-zA-Z0-9]|(?<![ -])[ -](?![ -])){1,}$', new_value):
            raise InvalidNameError("Value provided should be a proper name.")

        self._value = new_value.strip()
