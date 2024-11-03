# src/address_book/interface/commands.py
"""Module containing command definitions for the address book application."""
from __future__ import annotations

from enum import Enum
from typing import NamedTuple, Set


class CommandInfo(NamedTuple):
    """Structure for storing command information."""
    usage: str
    description: str
    command_name: str
    aliases: Set[str] = set()


class Commands(Enum):
    """Enumeration of all available commands and their usage information."""

    ADD = CommandInfo(
        usage="add [name] [phone]",
        description="Add a new contact or phone number",
        command_name="add"
    )

    CHANGE = CommandInfo(
        usage="change [name] [old phone] [new phone]",
        description="Change existing phone number",
        command_name="change"
    )

    PHONE = CommandInfo(
        usage="phone [name]",
        description="Show phone numbers for a contact",
        command_name="phone"
    )

    ADD_BIRTHDAY = CommandInfo(
        usage="add-birthday [name] [DD.MM.YYYY]",
        description="Add birthday for a contact",
        command_name="add-birthday"  # This is what will be used in the CLI
    )

    SHOW_BIRTHDAY = CommandInfo(
        usage="show-birthday [name]",
        description="Show birthday for a contact",
        command_name="show-birthday"
    )

    ALL = CommandInfo(
        usage="all",
        description="Show all contacts",
        command_name="all"
    )

    BIRTHDAYS = CommandInfo(
        usage="birthdays",
        description="Show upcoming birthdays",
        command_name="birthdays"
    )

    HELLO = CommandInfo(
        usage="hello",
        description="Get a greeting",
        command_name="hello"
    )

    EXIT = CommandInfo(
        usage="exit",
        description="Exit the program",
        command_name="exit",
        aliases={"close", "quit"}
    )

    HELP = CommandInfo(
        usage="help",
        description="Show available commands",
        command_name="help"
    )

    @property
    def help_message(self) -> str:
        """Get formatted help message for the command.

        Returns:
            str: Formatted usage and description.
        """
        aliases_str = f" (aliases: {', '.join(self.value.aliases)})" if self.value.aliases else ""
        return f"Usage: {self.value.usage} - {self.value.description}{aliases_str}"


    @classmethod
    def get_command(cls, command_name: str) -> Commands:
        """Get command enum by its string name.

        Args:
            command_name: The command name to look up.

        Returns:
            Commands: The corresponding command enum.

        Raises:
            ValueError: If command is not found.
        """
        command_name = command_name.lower()
        for command in cls:
            if (command.value.command_name == command_name or
                command_name in command.value.aliases):
                return command
        raise ValueError(f"Unknown command: {command_name}")


    @classmethod
    def get_all_commands(cls) -> str:
        """Get formatted string of all available commands.

        Returns:
            str: Newline-separated list of all command help messages.
        """
        return "\n".join(cmd.help_message for cmd in cls)
