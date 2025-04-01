from datetime import date
from pathlib import Path
from pprint import pformat

from classes.xlclass import Xlsx


def write_output_file(mor_nums: Xlsx, data: dict, formatted_date: date) -> None:
    """
    Write data to an Excel file using the Xlsx class.

    Parameters:
    mor_nums (Xlsx): An instance of the Xlsx class.
    data (dict): A dictionary containing the data to be written.
    formatted_date (date): The date to be written in the file.
    """
    mor_nums.set_matching_value(
        srchcol="F",
        srchval="Date Compiled",
        trgtcol="G",
        setval=formatted_date,
        startrow=3,
    )

    for volume_type in data.keys():
        mor_nums.set_matching_value(
            srchcol="A",
            srchval=volume_type,
            trgtcol="B",
            setval=data[volume_type],
            startrow=3,
        )

    mor_nums.save()


def output_py(data: dict, log_file: Path, formatted_date: date) -> None:
    """
    Append data to a log file.

    Parameters:
    data (dict): A dictionary containing the data to be logged.
    log_file (Path): The path to the log file.
    formatted_date (date): The date to be written in the log file.
    """
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(formatted_date)
        file.write(f"\n{pformat(data)}")
        file.write("\n" * 2)
