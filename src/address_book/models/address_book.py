# src/address_book/models/address_book.py
"""Module containing the AddressBook class for managing contacts.

This module provides the main AddressBook class which handles storage and
management of all contact records.
"""
from __future__ import annotations

from collections import UserDict
from datetime import datetime
from datetime import timedelta
from typing import Dict
from typing import List
from typing import Optional

from exceptions import RecordNotFoundException
from exceptions import ValidationError
from models import Record


class AddressBook(UserDict):
    """Class representing an address book.

    Inherits from UserDict to provide dictionary-like behavior for storing
    and managing contact records. Provides methods for adding, finding,
    and managing contacts and their birthdays.

    Attributes:
        data (Dict[str, Record]): Internal storage for contact records.
    """

    def add_record(self, record: Record) -> None:
        """Add a new record to the address book.

        Args:
            record: The Record object to add.

        Raises:
            ValidationError: If a record with this name already exists.
        """
        if record.name.value in self.data:
            raise ValidationError(f"Contact {record.name.value} already exists")
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name.

        Args:
            name: The name to search for.

        Returns:
            Optional[Record]: The found Record object or None if not found.
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by name.

        Args:
            name: The name of the record to delete.

        Raises:
            RecordNotFoundException: If the record is not found.
        """
        if name not in self.data:
            raise RecordNotFoundException(f"Contact {name} not found")
        del self.data[name]

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        """Get list of upcoming birthdays within the next week.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing name and
                congratulation date for contacts with upcoming birthdays.
                Each dictionary has 'name' and 'congratulation_date' keys.
        """
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() >= 5:
                    days_until_monday = (7 - congratulation_date.weekday()) + 1
                    congratulation_date += timedelta(days=days_until_monday)

                upcoming_birthdays.append({
                    "name": str(record.name),
                    "congratulation_date": congratulation_date.strftime('%d.%m.%Y'),
                })

        return upcoming_birthdays

    def __str__(self) -> str:
        """Return string representation of the address book.

        Returns:
            str: Formatted string of all contacts.
        """
        if not self.data:
            return "Address book is empty"
        return '\n'.join(str(record) for record in self.data.values())
