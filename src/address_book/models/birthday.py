# src/address_book/models/birthday.py
"""Module containing the Birthday field class.

This module provides the Birthday class for storing and validating contact
birthday dates in the address book system.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

from exceptions import InvalidBirthdayError
from models import Field


class Birthday(Field):
    """Class representing a contact's birthday.

    Extends the Field class with specific validation for birthday dates.
    Dates must be in DD.MM.YYYY format and cannot be in the future.

    Attributes:
        _value (datetime): Protected storage for the birthday date.
    """

    @property
    def value(self) -> datetime:
        """Get the stored birthday value.

        Returns:
            datetime: The stored birthday date.
        """
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Set the birthday value with validation.

        Args:
            new_value: Birthday date string in DD.MM.YYYY format.

        Raises:
            InvalidBirthdayError: If the date or its format is invalid or value is not a string or date is in the future.
        """
        if not isinstance(new_value, str):
            raise InvalidBirthdayError("Birthday must be a string in DD.MM.YYYY format")

        try:
            parsed_date = datetime.strptime(new_value.strip(), "%d.%m.%Y")
        except ValueError:
            raise InvalidBirthdayError(
                "Invalid date or its format. DD.MM.YYYY should be used",
            )

        if parsed_date > datetime.today():
            raise InvalidBirthdayError(
                f"Birthday cannot be in the future. Today is {datetime.today().strftime('%d.%m.%Y')}",
            )

        self._value = parsed_date

    def __str__(self) -> str:
        """Return string representation of the birthday value.

        Returns:
            str: String representation of the stored value.
        """
        return self.value.strftime('%d.%m.%Y')
