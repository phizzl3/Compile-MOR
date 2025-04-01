"""
This module provides a utility function to clear the console screen
based on the detected operating system.
"""

__version__ = "1.1.1"

import os
import platform


def clear_screen():
    """
    Clears the console screen based on the detected operating system.
    
    On Windows, it uses the 'cls' command.
    On other operating systems, it uses the 'clear' command.
    """
    os.system(f"{'cls' if platform.system() == 'Windows' else 'clear'}")


if __name__ == "__main__":
    """
    If this module is run as the main program, it will clear the console screen.
    """
    clear_screen()
