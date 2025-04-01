from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from classes.xlclass import Xlsx


@dataclass
class ConfigData:
    """
    Configuration data for the application.

    Attributes:
        today (date): The current date.
        formatted_date (str): The formatted date string.
        write_log_file (bool): Flag to indicate if log file should be written.
        open_output_file (bool): Flag to indicate if output file should be opened.
        bw_vol_regex (str): Regular expression for black and white volume.
        color_vol_regex (str): Regular expression for color volume.
        production_info (dict): Dictionary containing machine data.
        app_files (Path): Path to application files.
        working_folder (Path): Path to the working folder.
        default_values (bool): Flag to indicate if default values are being used.
    """

    today: date
    formatted_date: str
    write_log_file: bool
    open_output_file: bool
    bw_vol_regex: str
    color_vol_regex: str
    production_info: dict
    app_files: Path
    working_folder: Path
    default_values: bool


@dataclass
class FileObj:
    """
    File object containing various file paths and Xlsx objects.

    Attributes:
        mor_numbers_x (Xlsx): Xlsx object for MOR numbers.
        executive_summary_p (Path): Path to the executive summary.
        meter_reads_dump_x (Xlsx): Xlsx object for meter reads dump.
        copy_job_counts_x (Xlsx | None): Xlsx object for copy job counts, or None.
        mo_accuracy_x (Xlsx | None): Xlsx object for MO accuracy, or None.
        mo_timeliness_x (Xlsx | None): Xlsx object for MO timeliness, or None.
        log_file_p (Path): Path to the log file.
    """

    mor_numbers_x: Xlsx
    executive_summary_p: Path
    meter_reads_dump_x: Xlsx
    copy_job_counts_x: Xlsx | None
    mo_accuracy_x: Xlsx | None
    mo_timeliness_x: Xlsx | None
    log_file_p: Path


@dataclass
class MOR:
    """
    MOR data containing various fleet, mail, MPS, and production data.

    Attributes:
        fleet_data (dict): Dictionary containing fleet data.
        mail_data (dict): Dictionary containing mail data.
        mps_data (dict): Dictionary containing MPS data.
        production_data (dict): Dictionary containing production data.
    """

    fleet_data: dict = field(default_factory=dict)
    mail_data: dict = field(default_factory=dict)
    mps_data: dict = field(default_factory=dict)
    production_data: dict = field(default_factory=dict)
