"""
This module provides functionality to generate and return configuration data.
"""

from datetime import date
from pathlib import Path

from classes.dclasses import ConfigData
from config.defaults import DEFAULTS
from utils.loadconfig import load_config


def get_configuration_data() -> ConfigData:
    """
    Generates and returns configuration data.

    This function loads configuration data from a JSON file, applies default values,
    and returns a ConfigData object containing various configuration settings.

    Returns:
        ConfigData: An object containing configuration data.
    """
    today = date.today()
    working_folder = Path().home() / "Downloads"
    app_files = Path().home() / "PyAppFiles" / "Compile MOR"
    json_filepath = app_files / "config.json"
    json_data = load_config(json_path=json_filepath, default_data=DEFAULTS)

    return ConfigData(
        today=today,
        formatted_date=f"{today.month}/{today.day}/{today.year}",
        write_log_file=json_data["write log file"],
        open_output_file=json_data["open output file"],
        bw_vol_regex=json_data["grayscale volume regex"],
        color_vol_regex=json_data["color volume regex"],
        production_info=json_data["production info"],
        app_files=app_files,
        working_folder=working_folder,
        default_values=json_data["using default values"],
    )
