# src/address_book/models/record.py
"""Contact record implementation for the address book system.

This module provides the Record class which serves as a container for contact
information including name, phone numbers, and birthday.
"""
from __future__ import annotations

from exceptions import DuplicateBirthdayError
from exceptions import DuplicatePhoneError
from exceptions import PhoneNotFoundException
from models import Birthday
from models import Name
from models import Phone


class Record:
    """Container for contact information.

    Stores and manages a contact's details including name, multiple phone numbers,
    and an optional birthday.

    Args:
        name: The contact's name.

    Raises:
        EmptyNameError: If the name is empty.
        InvalidNameError: If the name format is invalid.
    """

    def __init__(self, name: str) -> None:
        """Initialize a new contact record.

        Args:
            name: The contact's name.
        """
        self._name: Name = Name(name)
        self._phones: list[Phone] = []
        self._birthday: Birthday | None = None

    @property
    def name(self) -> Name:
        """Get the contact's name.

        Returns:
            Name: The contact's name object.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the contact's name.

        Args:
            new_name: The new name for the contact.

        Raises:
            EmptyNameError: If the name is empty.
            InvalidNameError: If the name format is invalid.
        """
        self._name = Name(new_name)

    @property
    def phones(self) -> list[Phone]:
        """Get the contact's phone numbers.

        Returns:
            List of phone number objects.
        """
        return self._phones

    @property
    def birthday(self) -> Birthday | None:
        """Get the contact's birthday.

        Returns:
            Birthday object if set, None otherwise.
        """
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday: str | None) -> None:
        """Set the contact's birthday.

        Args:
            new_birthday: Birthday date string in DD.MM.YYYY format, or None to remove.

        Raises:
            InvalidBirthdayError: If the date format or value is invalid.
        """
        if new_birthday is None:
            self._birthday = None
        else:
            self._birthday = Birthday(new_birthday)

    def add_phone(self, phone_number: str) -> None:
        """Add a new phone number to the contact.

        Args:
            phone_number: Phone number to add.

        Raises:
            InvalidPhoneError: If the phone number format is invalid.
            DuplicatePhoneError: If the number already exists.
        """
        phone = Phone(phone_number)
        if self.find_phone(phone_number):
            raise DuplicatePhoneError(
                "This phone number already exists for this contact",
            )
        self._phones.append(phone)

    def remove_phone(self, phone_number: str) -> None:
        """Remove a phone number from the contact.

        Args:
            phone_number: Phone number to remove.

        Raises:
            PhoneNotFoundException: If the number is not found.
        """
        phone = self.find_phone(phone_number)
        if phone:
            self._phones.remove(phone)
        else:
            raise PhoneNotFoundException("Phone number not found for this contact")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number.

        Args:
            old_phone: Existing phone number to change.
            new_phone: New phone number.

        Raises:
            PhoneNotFoundException: If old number is not found.
            InvalidPhoneError: If new number format is invalid.
        """
        phone = self.find_phone(old_phone)
        if not phone:
            raise PhoneNotFoundException("Phone number not found for this contact")
        phone.value = new_phone

    def find_phone(self, phone_number: str) -> Phone | None:
        """Find a phone number in the contact's phones.

        Args:
            phone_number: Phone number to search for.

        Returns:
            Phone object if found, None otherwise.
        """
        return next((phone for phone in self._phones if phone.value == phone_number), None)

    def add_birthday(self, birthday_date: str) -> None:
        """Add a birthday date to the contact.

        Args:
            birthday_date: Birthday in DD.MM.YYYY format.

        Raises:
            DuplicateBirthdayError: If birthday is already set.
            InvalidBirthdayError: If date format or value is invalid.
        """
        if self._birthday:
            raise DuplicateBirthdayError("Birthday already exists for this contact")
        self._birthday = Birthday(birthday_date)

    def __str__(self) -> str:
        """Convert record to string representation.

        Returns:
            Formatted string with contact's details.
        """
        phones_str = ', '.join(str(p) for p in self._phones)
        birthday_str = str(self._birthday) if self._birthday else "not added yet"
        return f"Contact name: {self._name}; phones: {phones_str}; birthday: {birthday_str}"
