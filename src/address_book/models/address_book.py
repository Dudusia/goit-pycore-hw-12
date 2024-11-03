# src/address_book/models/address_book.py
"""Address Book implementation module.

This module provides the AddressBook class, which is the main container for managing
contacts in the address book system. It handles storage and retrieval of contact records,
and provides functionality for managing upcoming birthdays.
"""
from __future__ import annotations

from collections import UserDict
from datetime import datetime
from datetime import timedelta

from exceptions import RecordNotFoundException
from exceptions import DuplicateRecordException
from models import Record


class AddressBook(UserDict):
    """Main address book container for managing contacts.

    Inherits from UserDict to provide dictionary-like behavior for storing
    and managing contact records. Uses contact names as keys and Record
    objects as values.

    The class provides methods for adding, finding, and managing contacts,
    as well as tracking upcoming birthdays.

    Attributes:
        data: Dictionary storing contact records with names as keys.
            Inherited from UserDict.

    """

    def add_record(self, record: Record) -> None:
        """Add a new record to the address book.

        Args:
            record: A Record object containing contact information.

        Raises:
            DuplicateRecordException: If a contact with this name already exists.
        """
        if record.name.value in self.data:
            raise DuplicateRecordException(f"Contact {record.name.value} already exists")
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by contact name.

        Args:
            name: The name of the contact to find.

        Returns:
            The Record object if found, None otherwise.

        Example:
            >>> contact = book.find("Alice")
            >>> if contact:
            ...     print(contact.phones)  # Show Alice's phone numbers
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by contact name.

        Args:
            name: The name of the contact to delete.

        Raises:
            RecordNotFoundException: If no contact exists with the given name.

        Example:
            >>> try:
            ...     book.delete("Alice")  # Removes Alice from contacts
            ... except RecordNotFoundException:
            ...     print("Contact not found")
        """
        if name not in self.data:
            raise RecordNotFoundException(f"Contact {name} not found")
        del self.data[name]

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        """Get list of upcoming birthdays within the next week.

        Checks each contact's birthday and returns those occurring within
        the next 7 days. If a birthday falls on a weekend, the congratulation
        date is moved to the following Monday.

        Returns:
            List of dictionaries containing contact names and congratulation dates.
            Each dictionary has:
                - 'name': Contact's name
                - 'congratulation_date': Date to congratulate (DD.MM.YYYY format)

        Example:
            >>> birthdays = book.get_upcoming_birthdays()
            >>> for bd in birthdays:
            ...     print(f"Congratulate {bd['name']} on {bd['congratulation_date']}")

        Note:
            - Weekend birthdays are moved to the following Monday
            - Only includes birthdays within the next 7 days
            - Dates are returned in DD.MM.YYYY format
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

                if congratulation_date.weekday() >= 5:  # Weekend
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
            A string containing all contacts and their information,
            or "Address book is empty" if no contacts exist.

        Example:
            >>> print(book)  # Shows all contacts and their details
            Contact name: Alice; phones: 1234567890; birthday: 01.01.1990
            Contact name: Bob; phones: 9876543210; birthday: not added yet
        """
        if not self.data:
            return "Address book is empty"
        return '\n'.join(str(record) for record in self.data.values())
