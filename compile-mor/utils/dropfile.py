"""
This module provides utilities for handling file paths dropped by the user.
"""

__version__ = "1.1.1"

from pathlib import Path


def get_dropped_file() -> Path:
    """
    Prompts the user to drop a file and returns the resolved file path.

    Returns:
        Path: The resolved path of the dropped file.
    """
    file_location = input("\n Drop File: ")
    file_location = _clean_characters(file_location)
    return Path(file_location).resolve()


def _clean_characters(file_location: str) -> str:
    """
    Cleans up the file location string by removing unwanted characters.

    Args:
        file_location (str): The file location string to clean.

    Returns:
        str: The cleaned file location string.
    """
    file_location = file_location.strip(" &'\"")
    file_location = file_location.replace("\ ", " ")
    file_location = file_location.replace("''", "'")
    return file_location
