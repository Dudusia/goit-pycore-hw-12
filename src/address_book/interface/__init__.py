# src/address_book/interface/__init__.py
from __future__ import annotations

from .commands import Commands
from .cli_handler import CLIHandler

__all__ = ['Commands', 'CLIHandler']
