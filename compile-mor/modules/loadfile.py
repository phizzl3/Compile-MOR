from pathlib import Path

from classes.xlclass import Xlsx
from utils.dropfile import get_dropped_file


def load_data_source_file(
    filepath: Path, sheet_name: str = False, required=False
) -> Xlsx | None:
    """
    Load data from an Excel file.

    Parameters:
    filepath (Path): The path to the Excel file.
    sheet_name (str, optional): The name of the sheet to load. Defaults to False.
    required (bool, optional): If True, prompts the user to drop a file if the specified file is not found. Defaults to False.

    Returns:
    Xlsx | None: An Xlsx object if the file is found, otherwise None.
    """
    if not filepath.is_file():
        if required:
            print(f"\n {filepath.name} file not found in Downloads folder.")
            filepath = get_dropped_file()
        else:
            return None
    if sheet_name:
        return Xlsx(filepath, sheet_name)
    return Xlsx(filepath)
