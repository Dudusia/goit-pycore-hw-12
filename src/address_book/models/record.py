# src/address_book/models/record.py
"""Module containing the Record class for managing individual contacts.

This module provides the Record class which serves as a container for contact
information including name, phone numbers, and birthday.
"""
from __future__ import annotations

from typing import List
from typing import Optional

from exceptions import DuplicateBirthdayError
from exceptions import DuplicatePhoneError
from exceptions import PhoneNotFoundException
from models import Birthday
from models import Name
from models import Phone


class Record:
    """Class representing a contact record.

    Manages a contact's information including name, phone numbers, and birthday.
    Provides methods for adding, removing, and editing contact details.

    Attributes:
        _name (Name): The contact's name (protected).
        _phones (List[Phone]): List of the contact's phone numbers (protected).
        _birthday (Optional[Birthday]): The contact's birthday, if set (protected).
    """

    def __init__(self, name: str) -> None:
        """Initialize a new contact record.

        Args:
            name: The contact's name.

        Raises:
            EmptyNameError: If the name is empty.
            InvalidNameError: If the name is not a string or not a proper name.
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
            InvalidNameError: If the name is not a string or not a proper name.
        """
        self._name = Name(new_name)

    @property
    def phones(self) -> list[Phone]:
        """Get the contact's phone numbers.

        Returns:
            List[Phone]: List of phone number objects.
        """
        return self._phones

    @property
    def birthday(self) -> Birthday | None:
        """Get the contact's birthday.

        Returns:
            Optional[Birthday]: Birthday object if set, None otherwise.
        """
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday: str | None) -> None:
        """Set the contact's birthday.

        Args:
            new_birthday: Birthday date string in DD.MM.YYYY format or None.

        Raises:
            InvalidBirthdayError: If the date or its format is invalid or value is not a string or date is in the future.
        """
        if new_birthday is None:
            self._birthday = None
        else:
            self._birthday = Birthday(new_birthday)

    def add_phone(self, phone_number: str) -> None:
        """Add a new phone number to the contact.

        Args:
            phone_number: The phone number to add.

        Raises:
            InvalidPhoneError: If the phone number is not exactly 10 digits or not a string.
            DuplicatePhoneError: If phone number provided already exists for this contact.
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
            phone_number: The phone number to remove.

        Raises:
            PhoneNotFoundException: If the phone number is not found.
        """
        phone = self.find_phone(phone_number)
        if phone:
            self._phones.remove(phone)
        else:
            raise PhoneNotFoundException("Phone number not found for this contact")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number.

        Args:
            old_phone: The phone number to replace.
            new_phone: The new phone number.

        Raises:
            InvalidPhoneError: If the phone number is not exactly 10 digits or not a string.
            PhoneNotFoundException: If the old phone number is not found.
        """
        phone = self.find_phone(old_phone)
        if not phone:
            raise PhoneNotFoundException("Phone number not found for this contact")
        phone.value = new_phone

    def find_phone(self, phone_number: str) -> Phone | None:
        """Find a phone number in the contact's phones.

        Args:
            phone_number: The phone number to search for.

        Returns:
            Optional[Phone]: The found Phone object or None if not found.
        """
        return next((phone for phone in self._phones if phone.value == phone_number), None)

    def add_birthday(self, birthday_date: str) -> None:
        """Add a birthday date to the contact.

        Args:
            birthday_date: Birthday date in DD.MM.YYYY format.

        Raises:
            DuplicateBirthdayError: If birthday date is invalid or already exists.
        """
        if self._birthday:
            raise DuplicateBirthdayError("Birthday already exists for this contact")
        self._birthday = Birthday(birthday_date)

    def __str__(self) -> str:
        """Return string representation of the contact.

        Returns:
            str: Formatted string with contact's details.
        """
        phones_str = ', '.join(str(p) for p in self._phones)
        birthday_str = str(self._birthday) if self._birthday else "not added yet"
        return f"Contact name: {self._name}; phones: {phones_str}; birthday: {birthday_str}"
