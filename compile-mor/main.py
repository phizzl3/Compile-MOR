"""
Main module for the Compile-MOR application.

This module handles the initialization and execution of the MOR compilation process.
It includes functions for displaying messages, calculating various totals, writing output files,
writing log files, and opening the output file if configured to do so.
"""

__version__ = "1.1.0"

import warnings

from classes import MOR, ConfigData, FileObj
from config import get_configuration_data
from modules import (
    calculate_fleet_totals,
    calculate_mail_totals,
    calculate_mps_totals,
    calculate_production_totals,
    display_ascii_art,
    display_first_run_message,
    display_welcome_message,
    get_file_objects,
    output_py,
    write_output_file,
)
from utils import clear_screen, open_file

warnings.simplefilter("ignore")


def display_messages(default_flag: bool, file_path: str) -> None:
    """
    Clears the screen, displays ASCII art and a welcome message, then waits for user input.

    Args:
        default_flag (bool): Flag indicating if default values are used.
        file_path (str): Path to the application's working files location.
    """
    clear_screen()
    if default_flag:
        display_first_run_message(file_path)
    display_ascii_art(__version__)
    display_welcome_message()
    input()


def compile_totals(mor: MOR) -> dict:
    """
    Compiles totals from various data sources within the MOR object.

    Args:
        mor (MOR): The MOR object containing various data.

    Returns:
        dict: A dictionary containing compiled totals from mail, fleet, MPS, and production data.
    """
    dicts_list = (mor.mail_data, mor.fleet_data, mor.mps_data, mor.production_data)
    return {key: value for _dict in dicts_list for key, value in _dict.items()}


def calculate_fleet(files: FileObj, mor: MOR, CONFIG: ConfigData) -> None:
    """
    Calculates fleet totals and updates the MOR object.

    Args:
        files (FileObj): The file objects containing data.
        mor (MOR): The MOR object to be updated.
        CONFIG (ConfigData): Configuration data including regex patterns for volume calculations.
    """
    calculate_fleet_totals(
        exec_summary=files.executive_summary_p,
        data=mor.fleet_data,
        bw_vol_regex=CONFIG.bw_vol_regex,
        color_vol_regex=CONFIG.color_vol_regex,
    )


def calculate_production(files: FileObj, mor: MOR, CONFIG: ConfigData) -> None:
    """
    Calculates production totals and updates the MOR object.

    Args:
        files (FileObj): The file objects containing data.
        mor (MOR): The MOR object to be updated.
        CONFIG (ConfigData): Configuration data including machine data and current date.
    """
    calculate_production_totals(
        meters=files.meter_reads_dump_x,
        accuracy=files.mo_accuracy_x,
        timeliness=files.mo_timeliness_x,
        copy_jobs=files.copy_job_counts_x,
        data=mor.production_data,
        production_info=CONFIG.production_info,
        today=CONFIG.today,
    )


def calculate_mps(files: FileObj, mor: MOR) -> None:
    """
    Calculates MPS totals and updates the MOR object.

    Args:
        files (FileObj): The file objects containing data.
        mor (MOR): The MOR object to be updated.
    """
    calculate_mps_totals(mor_numbers=files.mor_numbers_x, data=mor.mps_data)


def calculate_mail(mor: MOR) -> None:
    """
    Calculates mail totals and updates the MOR object.

    Args:
        mor (MOR): The MOR object to be updated.
    """
    calculate_mail_totals(data=mor.mail_data)


def write_out(files: FileObj, compiled_totals: dict, CONFIG: ConfigData) -> None:
    """
    Writes the compiled totals to an output file.

    Args:
        files (FileObj): The file objects containing data.
        compiled_totals (dict): The compiled totals to be written.
        CONFIG (ConfigData): Configuration data including the formatted date.
    """
    write_output_file(
        mor_nums=files.mor_numbers_x,
        data=compiled_totals,
        formatted_date=CONFIG.formatted_date,
    )


def write_log(files: FileObj, compiled_totals: dict, CONFIG: ConfigData) -> None:
    """
    Writes the compiled totals to a log file if configured to do so.

    Args:
        files (FileObj): The file objects containing data.
        compiled_totals (dict): The compiled totals to be written.
        CONFIG (ConfigData): Configuration data including the log file path.
    """
    if CONFIG.write_log_file:
        output_py(
            data=compiled_totals,
            log_file=files.log_file_p,
            formatted_date=CONFIG.formatted_date,
        )


def open_output(files: FileObj, CONFIG: ConfigData) -> None:
    """
    Opens the output file if configured to do so.

    Args:
        files (FileObj): The file objects containing data.
        CONFIG (ConfigData): Configuration data including the flag to open the output file.
    """
    if CONFIG.open_output_file:
        open_file(file_path=files.mor_numbers_x.path)


if __name__ == "__main__":
    CONFIG: ConfigData = get_configuration_data()

    display_messages(CONFIG.default_values, CONFIG.app_files)

    mor: MOR = MOR()
    files: FileObj = get_file_objects(CONFIG.app_files, CONFIG.working_folder)

    calculate_fleet(files, mor, CONFIG)
    calculate_mps(files, mor)
    calculate_production(files, mor, CONFIG)
    calculate_mail(mor)

    compiled_totals: dict = compile_totals(mor)

    write_out(files, compiled_totals, CONFIG)
    write_log(files, compiled_totals, CONFIG)
    open_output(files, CONFIG)
