__version__ = "1.1.0"

import os
import platform

def open_file(file_path: str) -> None:
    """
    Open a file with the default application based on the operating system.

    Parameters:
    file_path (str): The path to the file to be opened.
    """
    if platform.system() == "Windows":
        os.startfile(file_path)
    else:
        os.system(f'open "{file_path}"')
