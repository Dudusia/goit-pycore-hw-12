# src/address_book/main.py
"""Main module for the Address Book application.

This module provides the command-line interface and core functionality for managing
contacts in an address book. It includes functions for adding, updating, and
viewing contact information including phone numbers and birthdays.

The module supports the following commands:
    - add [name] [phone]: Add a new contact or phone to existing contact
    - change [name] [old phone] [new phone]: Update existing phone number
    - phone [name]: Display contact's phone numbers
    - all: Display all contacts
    - add-birthday [name] [date]: Add birthday to contact
    - show-birthday [name]: Show contact's birthday
    - birthdays: Show upcoming birthdays
    - hello: Display greeting message
    - close/exit: Exit the program
"""
from __future__ import annotations

from exceptions import AddressBookException
from exceptions import RecordNotFoundException
from models import AddressBook
from models import Record
from config import Config
import pickle
from interface import Commands

def save_data(book, filename=Config.STORAGE_FILE_PATH):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename=Config.STORAGE_FILE_PATH):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def input_error(func):
    """Decorator that handles common input errors in contact management functions.

    This decorator catches and handles common exceptions that may occur during
    contact management operations, providing user-friendly error messages.

    Args:
        func: The function to be decorated.

    Returns:
        wrapper: Function that executes the decorated function within a try-except block.

    Handled Exceptions:
        ValueError: When required arguments are missing or invalid.
        KeyError: When operations are attempted on non-existent contacts.
        IndexError: When accessing invalid list indices.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AddressBookException as e:
            return str(e)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid number of arguments. Please check command format."
    return inner


@input_error
def parse_input(user_input):
    """Parses user input into command and arguments.

    Splits the input string into a command and its arguments, normalizing
    the command to lowercase.

    Args:
        user_input: String containing command and optional arguments.

    Returns:
        tuple: Contains command string and any additional arguments.

    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    """Adds a new contact or updates an existing contact in the address book.

    If the contact doesn't exist, creates a new contact with the provided name
    and phone number. If the contact exists, adds the new phone number to the
    existing contact.

    Args:
        args: List containing name and phone number.
        book: AddressBook instance to store the contact.

    Returns:
        str: Success message indicating whether contact was added or updated.

    Raises:
        ValueError: If required arguments are missing.
        DuplicatePhoneError: If phone number already exists for the contact.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        message = "Contact added."
        return message
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """Updates an existing phone number for a contact.

    Args:
        args: List containing name, old phone number, and new phone number.
        book: AddressBook instance containing the contact.

    Returns:
        str: Success message confirming the update.

    Raises:
        RecordNotFoundException: If contact is not found.
        PhoneNotFoundException: If old phone number doesn't exist.
        ValueError: If required arguments are missing or invalid.
    """
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
        raise RecordNotFoundException(f"Contact {name} not found")
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    """Displays all phone numbers for a specified contact.

    Args:
        args: List containing the contact name.
        book: AddressBook instance containing the contact.

    Returns:
        str: Newline-separated list of phone numbers.

    Raises:
        RecordNotFoundException: If contact is not found.
        ValueError: If required arguments are missing.
    """
    name, *_ = args
    record = book.find(name)
    if not record:
        raise RecordNotFoundException(f"Contact {name} not found")
    return "\n".join(f"{phone}" for phone in record.phones)


@input_error
def add_birthday(args, book: AddressBook):
    """Adds a birthday to an existing contact.

    Args:
        args: List containing name and birthday date (DD.MM.YYYY format).
        book: AddressBook instance containing the contact.

    Returns:
        str: Success message confirming birthday addition.

    Raises:
        RecordNotFoundException: If contact is not found or birthday already exists.
        InvalidBirthdayError: If date or its format is invalid or future date provided.
    """
    name, bd, *_ = args
    record = book.find(name)
    if not record:
        raise RecordNotFoundException(f"Contact {name} not found")
    record.add_birthday(bd)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    """Shows the birthday of a specified contact.

    Args:
        args: List containing the contact name.
        book: AddressBook instance containing the contact.

    Returns:
        str: Contact's birthday or message if no birthday is recorded.

    Raises:
        RecordNotFoundException: If contact is not found.
        ValueError: If required arguments are missing.
    """
    name, *_ = args
    record = book.find(name)
    if not record:
        raise RecordNotFoundException(f"Contact {name} not found")
    if not record.birthday:
        return "There is no birthday recorded yet."
    return record.birthday


@input_error
def birthdays(book: AddressBook):
    """Lists all upcoming birthdays within the next week.

    Returns formatted list of contacts with birthdays in the next 7 days,
    adjusting congratulation dates for weekends to the following Monday.

    Args:
        book: AddressBook instance containing contacts.

    Returns:
        str: Formatted list of upcoming birthdays or message if none found.
    """
    bd_list = book.get_upcoming_birthdays()
    if not bd_list:
        return "No upcoming birthdays."
    return "\n".join(f"Name: {bd['name']}, congratulation date: {bd['congratulation_date']}" for bd in bd_list)


def show_all(book: AddressBook):
    """Displays all contacts in the address book.

    Args:
        book: AddressBook instance containing contacts.

    Returns:
        str: Formatted string showing all contacts and their information.
    """
    return book


def main():
    """Main function that runs the address book application.

    Provides a command-line interface for interacting with the address book.
    Continuously accepts user commands until 'close' or 'exit' is entered.
    """
    book = load_data()
    print("Welcome to the assistant bot!")
    print("Available commands:")
    print(Commands.get_all_commands())
    command_handlers = {
      Commands.ADD.name.lower(): lambda: add_contact(args, book),
      Commands.CHANGE.name.lower(): lambda: change_contact(args, book),
      Commands.PHONE.name.lower(): lambda: show_phone(args, book),
      Commands.ALL.name.lower(): lambda: show_all(book),
      Commands.ADD_BIRTHDAY.name.lower(): lambda: add_birthday(args, book),
      Commands.SHOW_BIRTHDAY.name.lower(): lambda: show_birthday(args, book),
      Commands.BIRTHDAYS.name.lower(): lambda: birthdays(book),
      Commands.HELLO.name.lower(): lambda: "How can I help you?"
    }
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in command_handlers:
            print(command_handlers[command]())
        else:
            print("Invalid command. Available commands:")
            print(Commands.get_all_commands())

if __name__ == "__main__":
    main()
