# src/address_book/interface/cli_handler.py
from __future__ import annotations

from typing import Callable, List, Tuple

from models import AddressBook, Record
from exceptions import AddressBookException, RecordNotFoundException
from .commands import Commands

class CLIHandler:
    """Handles command-line interface interactions for the address book application."""

    def __init__(self, address_book: AddressBook):
        """Initialize CLI handler with an address book instance.

        Args:
            address_book: AddressBook instance to work with.
        """
        self.book = address_book
        self.running = True
        self._init_command_handlers()

    def _init_command_handlers(self) -> None:
        """Initialize the mapping of commands to their handler methods."""

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

        Args:
            func: Function to decorate.

        Returns:
            Wrapped function that handles exceptions.
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
            Tuple of command and list of arguments.
        """
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    def _handle_exit(self, *_) -> str:
        """Handle exit command.

        Returns:
            Goodbye message.
        """
        self.running = False
        return "Good bye!"

    @_input_error
    def _handle_add(self, args: List[str]) -> str:
        """Handle add command.

        Args:
            args: Command arguments [name, phone].

        Returns:
            Success message.
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
        """Handle change command.

        Args:
            args: Command arguments [name, old_phone, new_phone].

        Returns:
            Success message.
        """
        name, old_phone, new_phone, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."

    @_input_error
    def _handle_phone(self, args: List[str]) -> str:
        """Handle phone command.

        Args:
            args: Command arguments [name].

        Returns:
            Phone numbers for the contact.
        """
        name, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        return "\n".join(str(phone) for phone in record.phones)

    def _handle_all(self, _) -> str:
        """Handle all command.

        Returns:
            String representation of all contacts.
        """
        return str(self.book)

    @_input_error
    def _handle_add_birthday(self, args: List[str]) -> str:
        """Handle add-birthday command.

        Args:
            args: Command arguments [name, birthday].

        Returns:
            Success message.
        """
        name, birthday, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        record.add_birthday(birthday)
        return "Birthday added."

    @_input_error
    def _handle_show_birthday(self, args: List[str]) -> str:
        """Handle show-birthday command.

        Args:
            args: Command arguments [name].

        Returns:
            Contact's birthday information.
        """
        name, *_ = args
        record = self.book.find(name)
        if not record:
            raise RecordNotFoundException(f"Contact {name} not found")
        return str(record.birthday) if record.birthday else "No birthday set for this contact."

    def _handle_birthdays(self, _) -> str:
        """Handle birthdays command.

        Returns:
            List of upcoming birthdays.
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
            user_input: Raw user input string.

        Returns:
            Command execution result or error message.
        """
        command, args = self._parse_input(user_input)
        if command == "close":
            command = "exit"

        handler = self._command_handlers.get(command)
        if handler:
            return handler(args)
        return f"Invalid command. Available commands:\n{Commands.get_all_commands()}"

    def run(self) -> None:
        """Run the CLI interface loop."""
        print("Welcome to the assistant bot!")
        print("Available commands:")
        print(Commands.get_all_commands())

        while self.running:
            user_input = input("\nEnter a command: ")
            result = self.handle_command(user_input)
            print(result)
