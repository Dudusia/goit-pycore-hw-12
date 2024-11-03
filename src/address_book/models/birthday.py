# src/address_book/models/birthday.py
"""Birthday field implementation for the address book system.

This module provides the Birthday class for storing and validating contact
birthdays. It ensures dates are in the correct format and not in the future.

"""
from __future__ import annotations

from datetime import datetime
from typing import Any

from exceptions import InvalidBirthdayError
from models import Field


class Birthday(Field):
    """Field implementation for storing and validating birthday dates.

    The Birthday class ensures that dates are provided in the correct format
    (DD.MM.YYYY) and represent valid calendar dates that are not in the future.

    Args:
        value: Birthday date string in DD.MM.YYYY format.

    Raises:
        InvalidBirthdayError: If date string is invalid or represents a future date.

    Attributes:
        _value: Protected storage for the datetime object.
    """

    @property
    def value(self) -> datetime:
        """Get the stored birthday value.

        Returns:
            datetime: The stored birthday date.

        Example:
            >>> birthday = Birthday("01.01.1990")
            >>> print(birthday.value.strftime('%Y-%m-%d'))
            1990-01-01
        """
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Set and validate the birthday value.

        Args:
            new_value: Birthday date string in DD.MM.YYYY format.

        Raises:
            InvalidBirthdayError: If any of these conditions are met:
                - Input is not a string
                - Date format is incorrect (not DD.MM.YYYY)
                - Date is invalid (e.g., February 31st)
                - Date is in the future

        Example:
            >>> birthday = Birthday("01.01.1990")
            >>>
            >>> # This will raise InvalidBirthdayError (future date)
            >>> birthday.value = "01.01.2525"
            >>>
            >>> # This will raise InvalidBirthdayError (invalid format)
            >>> birthday.value = "1990-01-01"
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
        """Return string representation of the birthday.

        Returns:
            str: Birthday date in DD.MM.YYYY format.

        Example:
            >>> birthday = Birthday("01.01.1990")
            >>> str(birthday)
            '01.01.1990'
        """
        return self.value.strftime('%d.%m.%Y')
