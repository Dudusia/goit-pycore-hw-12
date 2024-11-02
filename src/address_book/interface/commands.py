"""Module containing command definitions for the address book application."""

from enum import Enum
from typing import NamedTuple

class CommandInfo(NamedTuple):
    """Structure for storing command information."""
    usage: str
    description: str

class Commands(Enum):
    """Enumeration of all available commands and their usage information."""

    ADD = CommandInfo(
        usage="add [name] [phone]",
        description="Add a new contact or phone number"
    )

    CHANGE = CommandInfo(
        usage="change [name] [old phone] [new phone]",
        description="Change existing phone number"
    )

    PHONE = CommandInfo(
        usage="phone [name]",
        description="Show phone numbers for a contact"
    )

    ADD_BIRTHDAY = CommandInfo(
        usage="add-birthday [name] [DD.MM.YYYY]",
        description="Add birthday for a contact"
    )

    SHOW_BIRTHDAY = CommandInfo(
        usage="show-birthday [name]",
        description="Show birthday for a contact"
    )

    ALL = CommandInfo(
        usage="all",
        description="Show all contacts"
    )

    BIRTHDAYS = CommandInfo(
        usage="birthdays",
        description="Show upcoming birthdays"
    )

    HELLO = CommandInfo(
        usage="hello",
        description="Get a greeting"
    )

    EXIT = CommandInfo(
        usage="close or exit",
        description="Exit the program"
    )

    @property
    def help_message(self) -> str:
        """Get formatted help message for the command.

        Returns:
            str: Formatted usage and description.
        """
        return f"Usage: {self.value.usage} - {self.value.description}"

    @classmethod
    def get_command(cls, command_name: str) -> 'Commands':
        """Get command enum by its string name.

        Args:
            command_name: The command name to look up.

        Returns:
            Commands: The corresponding command enum.

        Raises:
            ValueError: If command is not found.
        """
        try:
            return cls[command_name.upper().replace('-', '_')]
        except KeyError:
            raise ValueError(f"Unknown command: {command_name}")

    @classmethod
    def get_all_commands(cls) -> str:
        """Get formatted string of all available commands.

        Returns:
            str: Newline-separated list of all command help messages.
        """
        return "\n".join(cmd.help_message for cmd in cls)
