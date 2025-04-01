import calendar
from datetime import date

from classes.xlclass import Xlsx


def _read_production_volumes(meters: Xlsx, data: dict, production_info: dict) -> None:
    """
    Gather production totals from the meter reads data dump.

    Args:
        meters (Xlsx): The Xlsx object containing meter data.
        data (dict): The dictionary to store production volumes.
        production_info (dict): The dictionary containing machine data and meter columns.
    """
    print(" Gathering Production totals from", "Meter_Reads_Data_Dump.xlsx...", end="")

    for entry, info in production_info.items():
        if "machine" not in entry:
            continue
        for cell_contents, column in production_info["meter columns"].items():
            if "total" not in cell_contents:
                continue
            data[f'{info["name"]} {cell_contents}'] = meters.get_matching_value(
                srchcol=production_info["meter columns"]["serials"],
                srchval=info["serial number"],
                retcol=column,
                startrow=5,
            )

    print("Done.")


def _get_waste_input_from_user(disp: str) -> int:
    """
    Prompt the user to enter waste input.

    Args:
        disp (str): The display string for the waste type.

    Returns:
        int: The waste input entered by the user.
    """
    while True:
        user_input = input(f" Please enter {disp} waste: ")
        try:
            if user_input != "0" and user_input[0] != "-":
                user_input = f"-{user_input}"
        except IndexError:
            pass
        try:
            return int(user_input)
        except ValueError:
            pass
        print(" Please try again...")


def _get_waste_totals(data: dict) -> None:
    """
    Get waste totals from the user.

    Args:
        data (dict): The dictionary to store waste totals.
    """
    for key, display in (
        ("Black and White Waste", "Black and White"),
        ("Color Waste", "Color"),
    ):
        data[key] = _get_waste_input_from_user(disp=display)


def _get_reporting_month_year(today: date) -> str:
    """
    Get the reporting month and year based on the current date.

    Args:
        today (date): The current date.

    Returns:
        str: The reporting month and year.
    """
    month = today.month - 1 if today.month != 1 else 12
    year = today.year if month != 12 else today.year - 1
    return calendar.month_name[month], str(year) + ".0"


def _read_stats_file(
    acc_time: Xlsx, report_mo: str, report_yr: str, disp: str
) -> float | str:
    """
    Read statistics from the file.

    Args:
        acc_time (Xlsx): The Xlsx object containing statistics data.
        report_mo (str): The reporting month.
        report_yr (str): The reporting year.
        disp (str): The display string for the statistics type.

    Returns:
        float | str: The statistics value or "Not Found" if an error occurs.
    """
    print(f" {disp} file found.\n Reading file...")
    try:
        return (
            float(
                acc_time.search_matching_value(
                    header_srch_value=report_yr, row_srch_value=report_mo
                )
            )
            * 100
        )
    except TypeError:
        print(" Error reading.")
        return "Not Found"


def _read_jobs_file(copy_jobs: Xlsx) -> int | str:
    """
    Read the total jobs from the file.

    Args:
        copy_jobs (Xlsx): The Xlsx object containing jobs data.

    Returns:
        int | str: The total number of jobs or "Not Found" if an error occurs.
    """
    print(" Total Jobs file found.\n Reading file...")
    try:
        return int(
            copy_jobs.get_matching_value(
                srchcol="A", srchval="Total Jobs: ", retcol="A", startrow=9
            ).strip("Total Jobs: ")
        )
    except TypeError:
        print(" Error reading.")
        return "Not Found"


def _get_user_input(display: str, return_type: str) -> float | int:
    """
    Prompt the user to enter input.

    Args:
        display (str): The display string for the input type.
        return_type (str): The return type of the input ("f" for float, "i" for int).

    Returns:
        float | int: The user input.
    """
    while True:
        user_input = input(f" Please enter monthly {display}: ")
        try:
            return float(user_input) if return_type == "f" else int(user_input)
        except TypeError:
            print(" Please try again...")


def _get_production_stats(
    accuracy: Xlsx, timeliness: Xlsx, copy_jobs: Xlsx, data: dict, today: date
) -> None:
    """
    Get production statistics.

    Args:
        accuracy (Xlsx): The Xlsx object containing accuracy data.
        timeliness (Xlsx): The Xlsx object containing timeliness data.
        copy_jobs (Xlsx): The Xlsx object containing jobs data.
        data (dict): The dictionary to store production statistics.
        today (date): The current date.
    """
    if any((accuracy, timeliness)):
        report_month, report_year = _get_reporting_month_year(today=today)

    for key, file, display, return_type in (
        ("Job Accuracy", accuracy, "accuracy", "f"),
        ("Job Timeliness", timeliness, "timeliness", "f"),
    ):
        data[key] = (
            _read_stats_file(
                acc_time=file,
                report_mo=report_month,
                report_yr=report_year,
                disp=key,
            )
            if file
            else _get_user_input(display=display, return_type=return_type)
        )
    try:
        data["Number of Jobs"] = (
            _read_jobs_file(copy_jobs=copy_jobs)
            if copy_jobs
            else _get_user_input(display="jobs total", return_type="i")
        )
    except TypeError:
        data["Number of Jobs"] = "Error"


def calculate_production_totals(
    meters: Xlsx,
    accuracy: Xlsx,
    timeliness: Xlsx,
    copy_jobs: Xlsx,
    data: dict,
    production_info: dict,
    today: date,
) -> None:
    """
    Calculate production totals.

    Args:
        meters (Xlsx): The Xlsx object containing meter data.
        accuracy (Xlsx): The Xlsx object containing accuracy data.
        timeliness (Xlsx): The Xlsx object containing timeliness data.
        copy_jobs (Xlsx): The Xlsx object containing jobs data.
        data (dict): The dictionary to store production totals.
        production_info (dict): The dictionary containing machine data.
        today (date): The current date.
    """
    _read_production_volumes(
        meters=meters,
        data=data,
        production_info=production_info,
    )
    _get_waste_totals(data=data)
    _get_production_stats(
        accuracy=accuracy,
        timeliness=timeliness,
        copy_jobs=copy_jobs,
        data=data,
        today=today,
    )
