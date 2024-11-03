# Address Book CLI Application

A command-line address book application built in Python using object-oriented programming principles. The project features a clean, modular architecture with comprehensive data validation, birthday tracking capabilities, and robust error handling.

## Project Structure and Dependencies

```
address_book/
├── models/
│   ├── __init__.py        # Exports all model classes
│   ├── field.py           # Abstract base class, no dependencies
│   ├── name.py           # Depends on: field.py, exceptions
│   ├── phone.py          # Depends on: field.py, exceptions
│   ├── birthday.py       # Depends on: field.py, exceptions
│   ├── record.py         # Depends on: name.py, phone.py, birthday.py, exceptions
│   └── address_book.py   # Depends on: record.py, exceptions
├── exceptions/
│   ├── __init__.py       # Exports all exceptions
│   └── exceptions.py     # No dependencies
├── interface/
│   ├── __init__.py       # Exports interface components
│   ├── commands.py       # No dependencies
│   └── cli_handler.py    # Depends on: commands.py, models, exceptions
├── config.py             # No dependencies
└── main.py              # Depends on: config.py, models, interface
```

### Module Dependencies Explained

1. Base Modules (No Dependencies):
   - `exceptions/exceptions.py`: Defines base exception hierarchy
   - `models/field.py`: Abstract base class for fields
   - `config.py`: Application configuration
   - `interface/commands.py`: Command definitions

2. Field Implementations:
   - `models/name.py`, `phone.py`, `birthday.py`
   - Depend on: `field.py` and `exceptions`
   - Handle specific field validation and storage

3. Record Management:
   - `models/record.py`
   - Depends on: all field implementations and exceptions
   - Manages individual contact data

4. Address Book:
   - `models/address_book.py`
   - Depends on: `record.py` and exceptions
   - Handles contact collection and birthday tracking

5. Interface:
   - `interface/cli_handler.py`
   - Depends on: `commands.py`, models package, and exceptions
   - Manages user interaction

6. Application Entry:
   - `main.py`
   - Depends on: config, models, and interface packages
   - Handles initialization and data persistence

[Rest of the original content remains the same until "Installation"]

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/address-book.git
cd address-book
```

2. Ensure you have Python 3.7 or higher installed:
```bash
python --version
```

3. No additional package installation is required as the application uses only Python standard library.

## Class Structure

### Models Package (`models/`)

#### Field (`field.py`)
Abstract base class for all field types:
```python
from models import Field

class CustomField(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value  # Add validation as needed
```

#### Name (`name.py`)
Handles contact names with validation:
```python
from models import Name

name = Name("John Doe")  # Valid
name = Name("")         # Raises EmptyNameError
name = Name("John-2")   # Valid - supports letters, numbers, and hyphens
name = Name("-John")    # Raises InvalidNameError - can't start with hyphen
```

#### Phone (`phone.py`)
Manages phone numbers with validation:
```python
from models import Phone

phone = Phone("1234567890")    # Valid
phone = Phone("123 456 7890")  # Valid - spaces are stripped
phone = Phone("123")           # Raises InvalidPhoneError
phone = Phone("abcd")          # Raises InvalidPhoneError
```

#### Birthday (`birthday.py`)
Handles contact birthdays with validation:
```python
from models import Birthday

birthday = Birthday("01.01.1990")  # Valid
birthday = Birthday("31.02.1990")  # Raises InvalidBirthdayError - invalid date
birthday = Birthday("01.01.2025")  # Raises InvalidBirthdayError - future date
```

#### Record (`record.py`)
Manages individual contacts with multiple phones and birthday:
```python
from models import Record

record = Record("John Doe")
record.add_phone("1234567890")
record.add_phone("9876543210")        # Add multiple phones
record.add_birthday("01.01.1990")     # Add birthday
record.remove_phone("1234567890")
record.edit_phone("9876543210", "1112223333")
```

#### AddressBook (`address_book.py`)
Main container for all contacts with birthday tracking:
```python
from models import AddressBook, Record

book = AddressBook()
record = Record("John Doe")
book.add_record(record)
found = book.find("John Doe")
upcoming = book.get_upcoming_birthdays()  # Get birthdays in next 7 days
book.delete("John Doe")
```

## Command-Line Interface

The application supports the following commands:

```bash
# Adding contacts and phones
add [name] [phone]                    # Add new contact or phone
change [name] [old phone] [new phone] # Change existing phone
phone [name]                          # Show contact's phones
all                                   # Show all contacts

# Birthday management
add-birthday [name] [date]            # Add birthday (DD.MM.YYYY)
show-birthday [name]                  # Show contact's birthday
birthdays                             # Show upcoming birthdays

# Other commands
hello                                 # Show greeting
close or exit                         # Exit program
```

## Validation Rules

### Name Validation
- Must start with a letter
- Can contain letters, numbers, hyphens, and spaces
- Cannot have consecutive hyphens or spaces
- Cannot be empty
- Must match regex: `^[a-zA-Z](?:[a-zA-Z0-9]|(?<![ -])[ -](?![ -])){1,}$`

### Phone Validation
- Must be exactly 10 digits
- Can contain spaces or common separators (automatically stripped)
- Must be provided as string
- No duplicate phones per contact

### Birthday Validation
- Must be in DD.MM.YYYY format
- Must be a valid calendar date
- Cannot be in the future
- Only one birthday per contact

## Error Handling

The application uses a custom exception hierarchy:

```
AddressBookException
├── ValidationError
│   ├── PhoneError
│   │   ├── InvalidPhoneError
│   │   ├── DuplicatePhoneError
│   │   └── PhoneNotFoundException
│   ├── NameError
│   │   ├── EmptyNameError
│   │   └── InvalidNameError
│   └── BirthdayError
│       ├── InvalidBirthdayError
│       └── DuplicateBirthdayError
└── RecordNotFoundException
```

Example error handling:
```python
try:
    record.add_phone("123")
except InvalidPhoneError as e:
    print(e)  # "Phone number must be exactly 10 digits"

try:
    book.delete("Jane")
except RecordNotFoundException as e:
    print(e)  # "Contact Jane not found"
```

## Features

- Multiple phone numbers per contact
- Birthday tracking with upcoming birthday functionality
- Weekend adjustment for birthday congratulations
- Comprehensive input validation
- User-friendly error messages
- Command-line interface with input error handling
- No external dependencies

## Future Improvements

1. Data Persistence
   - Add save/load functionality
   - Support multiple storage backends (JSON, SQLite)

2. Additional Fields
   - Email addresses
   - Physical addresses
   - Notes
   - Custom fields

3. Enhanced Functionality
   - Search by phone number
   - Partial name matching
   - Contact groups/categories
   - Import/export (CSV, vCard)
   - Birthday reminders

4. User Interface
   - Add command history
   - Interactive mode improvements
   - Colored output
   - Help system

## Dependencies
- Python 3.7+
- Standard Library Modules:
  - `abc`: For abstract base classes
  - `collections`: For UserDict
  - `datetime`: For date handling
  - `pickle`: For data persistence
  - `pathlib`: For file path handling
  - `typing`: For type hints
  - `re`: For name validation patterns
  - `logging`: For error logging

No external packages required.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
