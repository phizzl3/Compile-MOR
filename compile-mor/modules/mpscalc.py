from classes.xlclass import Xlsx


def _read_mps_from_output_file(mor_numbers: Xlsx, data: dict) -> None:
    """Reads MPS totals from the previous month's output file and updates the data dictionary."""
    print(" Reading MDS totals from previous month...", end="")
    for search_term in ("Number of Ricoh Devices", "Number of Non-Networked Devices"):
        data[search_term] = mor_numbers.get_matching_value(
            srchcol="A", srchval=search_term, retcol="B", startrow=3
        )
    print("Done")


def _set_zero_starts(data: dict) -> None:
    """Sets initial values for equipment adds and moves to zero in the data dictionary."""
    data.update(
        {search_term: 0 for search_term in ("Equipment Adds", "Equipment Moves")}
    )


def _ask_for_changes(disp: str) -> bool:
    """Prompts the user to confirm if there were any changes (adds or moves) for the specified type of machine.

    Args:
        disp (str): Description of the machine change type (e.g., 'added', 'moved').

    Returns:
        bool: True if there were changes, False otherwise.
    """
    while True:
        answer = input(f" Where there any machines {disp}? (y/n): ")
        try:
            if answer[0].lower() in ("y", "n"):
                return answer[0].lower() == "y"
        except IndexError:
            pass
        print(" Please try again... (y/n)")


def _ask_for_new_numbers(disp: str) -> int:
    """Prompts the user to enter the number of machines for the specified type of change.

    Args:
        disp (str): Description of the machine change type (e.g., 'adds', 'moves').

    Returns:
        int: The number of machines entered by the user.
    """
    while True:
        answer = input(f"\n Enter number of machine {disp}: ")
        try:
            return int(answer)
        except ValueError:
            pass
        print(" Please try again... (#'s)")


def _check_for_updates(data: dict) -> None:
    """Checks for updates in equipment adds and moves, and updates the data dictionary accordingly."""
    added = _ask_for_changes("added")
    moved = _ask_for_changes("moved")
    if not any((added, moved)):
        return
    if added:
        adds = _ask_for_new_numbers("adds")
        data["Equipment Adds"] += adds
        data["Number of Ricoh Devices"] += adds
    if moved:
        data["Equipment Moves"] += _ask_for_new_numbers("moves")


def calculate_mps_totals(mor_numbers: Xlsx, data: dict):
    """Calculates and updates the MPS totals.

    Args:
        mor_numbers (Xlsx): An instance of the Xlsx class containing the MPS data.
        data (dict): A dictionary to store the MPS totals.
    """
    _read_mps_from_output_file(mor_numbers=mor_numbers, data=data)
    _set_zero_starts(data=data)
    _check_for_updates(data=data)
