# src/address_book/interface/__init__.py
"""Interface package for the address book system.

This package provides the user interface components for the address book system,
including command-line interface handling and command definitions.

The package consists of two main components:
    - Commands: Enumeration defining all available commands and their usage information
    - CLIHandler: Class that manages command-line interface interactions

Example:
    >>> from address_book.models import AddressBook
    >>> from address_book.interface import CLIHandler
    >>>
    >>> # Create an address book and CLI handler
    >>> book = AddressBook()
    >>> handler = CLIHandler(book)
    >>>
    >>> # Run the CLI interface
    >>> handler.run()

Note:
    The interface package is designed to be extensible, allowing for additional
    interface types (like GUI or web interface) to be added in the future while
    maintaining consistent command handling.
"""
from __future__ import annotations

from .commands import Commands
from .cli_handler import CLIHandler

__all__ = ['Commands', 'CLIHandler']
