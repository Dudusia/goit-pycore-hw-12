# src/address_book/interface/cli_handler.py
"""Command Line Interface handler for the address book system.

This module provides the CLIHandler class which manages all command-line
interactions with the address book system. It processes user input, executes
corresponding commands, and returns formatted responses.
"""
from __future__ import annotations

from typing import Callable, List, Tuple

from models import AddressBook, Record
from exceptions import AddressBookException, RecordNotFoundException, DuplicateRecordException
from interface import Commands


class CLIHandler:
    """Handles command-line interface interactions for the address book application.

    This class manages user interactions through the command line, processes commands,
    and executes corresponding operations on the address book.

    Args:
        address_book: An instance of AddressBook to operate on.

    Attributes:
        book: The AddressBook instance being managed.
        running: Boolean indicating if the CLI is actively running.

    Example:
        >>> book = AddressBook()
        >>> handler = CLIHandler(book)
        >>> handler.run()  # Starts the interactive CLI session
    """

    def __init__(self, address_book: AddressBook):
        """Initialize CLI handler with an address book instance.

        Args:
            address_book: AddressBook instance to work with.
        """
        self.book = address_book
        self.running = True
        self._init_command_handlers()

    def _init_command_handlers(self) -> None:
        """Initialize the mapping of commands to their handler methods.

        Sets up the dictionary mapping command names to their corresponding
        handler methods. This internal method is called during initialization.
        """
        self._command_handlers = {
            Commands.ADD.value.command_name: self._handle_add,
            Commands.CHANGE.value.command_name: self._handle_change,
            Commands.PHONE.value.command_name: self._handle_phone,
            Commands.ALL.value.command_name: self._handle_all,
            Commands.ADD_BIRTHDAY.value.command_name: self._handle_add_birthday,
            Commands.SHOW_BIRTHDAY.value.command_name: self._handle_show_birthday,
            Commands.BIRTHDAYS.value.command_name: self._handle_birthdays,
            Commands.HELLO.value.command_name: lambda _: "How can I help you?",
            Commands.EXIT.value.command_name: self._handle_exit,
            Commands.HELP.value.command_name: lambda _: Commands.get_all_commands(),
        }

    def _input_error(func: Callable) -> Callable:
        """Decorator for handling input errors in command handlers.

        Wraps command handler methods to catch and handle common exceptions,
        providing user-friendly error messages.

        Args:
            func: The function to decorate.

        Returns:
            A wrapped function that handles exceptions.

        Example:
            >>> @_input_error
            ... def handler(self, args):
            ...     # Function code that might raise exceptions
            ...     pass
        """
        def inner(self, *args, **kwargs) -> str:
            try:
                return func(self, *args, **kwargs)
            except AddressBookException as e:
                return str(e)
            except ValueError:
                return "Give me name and phone please."
            except KeyError:
                return "Contact not found."
            except IndexError:
                return "Invalid number of arguments. Please check command format."
        return inner

    @_input_error
    def _parse_input(self, user_input: str) -> Tuple[str, List[str]]:
        """Parse user input into command and arguments.

        Args:
            user_input: Raw user input string.

        Returns:
            A tuple containing:
                - The command string (lowercase)
                - List of command arguments

        Example:
            >>> handler._parse_input("add John 1234567890")
            ('add', ['John', '1234567890'])
        """
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    def _handle_exit(self, *_) -> str:
        """Handle the exit command.

        Sets the running flag to False and returns goodbye message.

        Returns:
            A farewell message string.
        """
        self.running = False
        return "Good bye!"

    @_input_error
    def _handle_add(self, args: List[str]) -> str:
        """Handle the add command.

        Creates a new contact or adds a phone number to an existing contact.

        Args:
            args: List containing [name, phone].

        Returns:
            Success message string.

        Raises:
            IndexError: If insufficient arguments provided.
            InvalidPhoneError: If phone number is invalid.
        """
        name, phone, *_ = args
        record = self.book.find(name)
        if record is None:
            record = Record(name)
            record.add_phone(phone)
            self.book.add_record(record)
            return "Contact added."
        record.add_phone(phone)
        return "Contact updated."

    @_input_error
    def _handle_change(self, args: List[str]) -> str:
        """Handle the change command.

        Updates an existing phone number for a contact.

        Args:
            args: List containing [name, old_phone, new_phone].

        Returns:
            Success message string.

        Raises:
            RecordNotFoundException: If contact is not found.
            IndexError: If insufficient arguments provided.
            InvalidPhoneError: If phone number is invalid.
        """
        name, old_phone, new_phone, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."

    @_input_error
    def _handle_phone(self, args: List[str]) -> str:
        """Handle the phone command.

        Retrieves phone numbers for a specified contact.

        Args:
            args: List containing [name].

        Returns:
            String containing all phone numbers for the contact.

        Raises:
            RecordNotFoundException: If contact is not found.
            IndexError: If name argument is missing.
        """
        name, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        return "\n".join(str(phone) for phone in record.phones)

    def _handle_all(self, _) -> str:
        """Handle the all command.

        Returns:
            String representation of all contacts.
        """
        return str(self.book)

    @_input_error
    def _handle_add_birthday(self, args: List[str]) -> str:
        """Handle the add-birthday command.

        Adds a birthday to an existing contact.

        Args:
            args: List containing [name, birthday].

        Returns:
            Success message string.

        Raises:
            RecordNotFoundException: If contact is not found.
            IndexError: If insufficient arguments provided.
            InvalidBirthdayError: If the date or its format is invalid or value is not a string or date is in the future.
        """
        name, birthday, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        record.add_birthday(birthday)
        return "Birthday added."

    @_input_error
    def _handle_show_birthday(self, args: List[str]) -> str:
        """Handle the show-birthday command.

        Retrieves birthday information for a specified contact.

        Args:
            args: List containing [name].

        Returns:
            String containing contact's birthday or a message if not set.

        Raises:
            RecordNotFoundException: If contact is not found.
            IndexError: If name argument is missing.
        """
        name, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        return str(record.birthday) if record.birthday else "No birthday set for this contact."

    def _handle_birthdays(self, _) -> str:
        """Handle the birthdays command.

        Retrieves list of upcoming birthdays.

        Returns:
            String containing upcoming birthdays information.
        """
        birthdays = self.book.get_upcoming_birthdays()
        if not birthdays:
            return "No upcoming birthdays."
        return "\n".join(
            f"Name: {bd['name']}, congratulation date: {bd['congratulation_date']}"
            for bd in birthdays
        )

    def handle_command(self, user_input: str) -> str:
        """Process a user command and return the result.

        Args:
            user_input: Raw input string from user.

        Returns:
            Response string from command execution.

        Example:
            >>> handler.handle_command("add John 1234567890")
            'Contact added.'
        """
        command, args = self._parse_input(user_input)
        if command == "close":
            command = "exit"

        handler = self._command_handlers.get(command)
        if handler:
            return handler(args)
        return f"Invalid command. Available commands:\n{Commands.get_all_commands()}"

    def run(self) -> None:
        """Run the CLI interface loop.

        Starts the interactive command-line interface, continuously processing
        user input until an exit command is received.

        Example:
            >>> handler = CLIHandler(AddressBook())
            >>> handler.run()
            Welcome to the assistant bot!
            Available commands:
            ...
        """
        print("Welcome to the assistant bot!")
        print("Available commands:")
        print(Commands.get_all_commands())

        while self.running:
            user_input = input("\nEnter a command: ")
            result = self.handle_command(user_input)
            print(result)
