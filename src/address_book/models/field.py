# src/address_book/models/field.py
"""Abstract base field implementation for the address book system.

This module provides the Field abstract base class which serves as the foundation
for all value fields in the address book system (Name, Phone, Birthday).
It defines the common interface and basic functionality that all field
implementations must follow.

"""
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class Field(ABC):
    """Abstract base class for all field types in the address book.

    This class defines the interface that all field classes must implement,
    providing basic value storage and validation functionality.
    Subclasses must implement the value property with appropriate
    validation rules.

    Args:
        value: Initial value for the field.

    Raises:
        ValueError: If the value is invalid according to field-specific validation.
    """

    def __init__(self, value: Any) -> None:
        """Initialize the field with a value.

        Args:
            value: Initial value for the field.

        Raises:
            ValueError: If value is invalid according to field-specific validation.

        Note:
            The validation is performed by the value setter, which must be
            implemented by subclasses.
        """
        self._value: Any = None
        self.value = value

    @property
    @abstractmethod
    def value(self) -> Any:
        """Get the stored field value.

        This property must be implemented by all subclasses to provide
        proper type hints and any necessary value transformation.

        Returns:
            The stored value in the appropriate type for the field.

        Raises:
            NotImplementedError: If the subclass doesn't implement this property.

        Example:
            >>> class StringField(Field):
            ...     @property
            ...     def value(self) -> str:
            ...         return self._value
        """
        return self._value

    @value.setter
    @abstractmethod
    def value(self, new_value: Any) -> None:
        """Set and validate the field value.

        This setter must be implemented by all subclasses to perform
        appropriate validation and type conversion.

        Args:
            new_value: The new value to validate and store.

        Raises:
            NotImplementedError: If the subclass doesn't implement this setter.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Return string representation of the field value.

        Returns:
            str: String representation of the stored value.
        """
        return str(self.value)

    def __eq__(self, other: Any) -> bool:
        """Compare this field with another value for equality.

        Allows comparison with both other Field objects and raw values.

        Args:
            other: Another field or value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        if isinstance(other, Field):
            return self.value == other.value
        return self.value == other
