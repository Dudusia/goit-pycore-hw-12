# Address Book CLI Application

A command-line address book application built in Python using object-oriented programming principles. The project features a clean, modular architecture with comprehensive data validation, birthday tracking capabilities, and robust error handling.

## Project Structure

```
address_book/
├── models/
│   ├── __init__.py        # Package initialization and exports
│   ├── field.py           # Abstract base field class
│   ├── name.py            # Name field implementation
│   ├── phone.py           # Phone field implementation
│   ├── birthday.py        # Birthday field implementation
│   ├── record.py          # Contact record class
│   └── address_book.py    # Main address book container
├── exceptions/
│   ├── __init__.py        # Exception exports
│   └── exceptions.py      # Custom exception definitions
└── main.py                # Application entry point
```

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
- No external packages required

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
