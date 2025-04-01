"""
This module provides a utility function to check if specified files exist at their given paths.
If a file is not found:
    - It creates the necessary parent directories.
    - It prompts the user to place the missing file in the specified directory.

Functions:
    check_paths(*args): Checks if the specified files exist and handles missing files.
"""

__version__ = "1.0.0"

from pathlib import Path

def check_paths(*args) -> None:
    """
    Checks if the specified files exist at their given paths.
    If a file is not found:
    - It creates the necessary parent directories.
    - It prompts the user to place the missing file in the specified directory.

    Args:
        *args: Multiple str or pathlib.Path objects representing file paths.
    """
    for file_path in args:
        check_path = Path(file_path)
        while True:
            if not check_path.exists():
                if not check_path.parent.is_dir():
                    check_path.parent.mkdir(parents=True)
                print(f"\n File: '{check_path.name}' not found.")
                print("\n Place the file in the following directory and press Enter:")
                input(f" '{check_path.parent}'")
            else:
                break
