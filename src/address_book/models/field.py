# src/address_book/models/field.py
"""Module containing the base Field class for the address book system.

This module provides the abstract base class Field which serves as the foundation
for all field types in the address book (Name, Phone, Birthday). It implements
basic functionality and defines the interface that all field classes must follow.
"""
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class Field(ABC):
    """Abstract base class for all fields in the address book.

    This class serves as a parent class for specific field types like Name, Phone,
    and Birthday, providing basic functionality for value storage and validation.
    All field classes must implement the value property with appropriate validation.

    Attributes:
        _value: Protected storage for the field's value.
    """

    def __init__(self, value: Any) -> None:
        """Initialize a new field with a value.

        Args:
            value: Initial value for the field.

        Raises:
            ValueError: If the value is invalid according to field-specific validation.
        """
        self._value: Any = None
        self.value = value

    @property
    @abstractmethod
    def value(self) -> Any:
        """Get the stored field value.

        This property must be implemented by all subclasses with appropriate
        type hints and validation.

        Returns:
            Any: The stored value in the appropriate type for the field.

        Raises:
            NotImplementedError: If the subclass doesn't implement this property.
        """
        return self._value

    @value.setter
    @abstractmethod
    def value(self, new_value: Any) -> None:
        """Set the field value with validation.

        This setter must be implemented by all subclasses with appropriate
        validation rules.

        Args:
            new_value: The new value to store.

        Raises:
            NotImplementedError: If the subclass doesn't implement this setter.
            ValueError: If the value is invalid according to field-specific rules.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Return string representation of the field value.

        Returns:
            str: String representation of the stored value.
        """
        return str(self.value)

    def __eq__(self, other: Any) -> bool:
        """Compare this field with another for equality.

        Args:
            other: Another field or value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        if isinstance(other, Field):
            return self.value == other.value
        return self.value == other
