# src/address_book/interface/commands.py
"""Command definitions for the address book application.

This module defines the available commands and their properties using an enumeration.
Each command has associated usage information, description, and optional aliases.

Example:
    >>> from interface.commands import Commands
    >>> # Get information about the add command
    >>> Commands.ADD.value.usage
    'add [name] [phone]'
    >>> Commands.ADD.value.description
    'Add a new contact or phone number'
"""
from __future__ import annotations

from enum import Enum
from typing import NamedTuple, Set


class CommandInfo(NamedTuple):
    """Structure for storing command information.

    Args:
        usage: String showing command usage syntax.
        description: String describing what the command does.
        command_name: String identifier for the command.
        aliases: Set of alternative names for the command. Defaults to empty set.

    Example:
        >>> cmd_info = CommandInfo(
        ...     usage="example [arg]",
        ...     description="An example command",
        ...     command_name="example",
        ...     aliases={"ex", "e"}
        ... )
    """
    usage: str
    description: str
    command_name: str
    aliases: Set[str] = set()


class Commands(Enum):
    """Enumeration of all available commands and their usage information.

    Each enum value is a CommandInfo instance containing the command's usage
    information, description, and any aliases.

    Attributes:
        ADD: Add a new contact or phone number.
        CHANGE: Change an existing phone number.
        PHONE: Display phone numbers for a contact.
        ADD_BIRTHDAY: Add birthday for a contact.
        SHOW_BIRTHDAY: Show birthday for a contact.
        ALL: Show all contacts.
        BIRTHDAYS: Show upcoming birthdays.
        HELLO: Display greeting message.
        EXIT: Exit the program.
        HELP: Show available commands.

    Example:
        >>> Commands.ADD.value
        CommandInfo(usage='add [name] [phone]',
                   description='Add a new contact or phone number',
                   command_name='add',
                   aliases=set())
    """

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
        command_name="add-birthday"
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
            A string containing the command's usage and description,
            including any aliases if present.

        Example:
            >>> Commands.EXIT.help_message
            'Usage: exit - Exit the program (aliases: close, quit)'
        """
        aliases_str = f" (aliases: {', '.join(self.value.aliases)})" if self.value.aliases else ""
        return f"Usage: {self.value.usage} - {self.value.description}{aliases_str}"

    @classmethod
    def get_command(cls, command_name: str) -> Commands:
        """Get command enum by its string name or alias.

        Args:
            command_name: The command name or alias to look up.

        Returns:
            The corresponding Commands enum value.

        Raises:
            ValueError: If the command name is not found.

        Example:
            >>> Commands.get_command("exit")
            <Commands.EXIT>
            >>> Commands.get_command("close")  # alias
            <Commands.EXIT>
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
            A newline-separated string listing all commands with their
            usage information, descriptions, and aliases.

        Example:
            >>> print(Commands.get_all_commands())
            Usage: add [name] [phone] - Add a new contact or phone number
            Usage: change [name] [old phone] [new phone] - Change existing phone number
            ...
        """
        return "\n".join(cmd.help_message for cmd in cls)
