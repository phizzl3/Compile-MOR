from pathlib import Path

from classes.dclasses import FileObj
from modules.loadfile import load_data_source_file
from utils.pathchecker import check_paths


def get_file_objects(app_files: Path, working_folder: Path) -> FileObj:
    """
    Generates and returns file access objects.

    Args:
        app_files (Path): The path to the application files.
        working_folder (Path): The path to the working folder.

    Returns:
        FileObj: An object containing file paths and loaded data sources.
    """
    check_paths(app_files / "MOR_Numbers.xlsx")

    return FileObj(
        mor_numbers_x=load_data_source_file(
            filepath=app_files / "MOR_Numbers.xlsx",
            sheet_name="Data Entry",
            required=True,
        ),
        executive_summary_p=working_folder / "Executive summary.pdf",
        meter_reads_dump_x=load_data_source_file(
            filepath=working_folder / "Meter_Reads_Data_Dump.xlsx", required=True
        ),
        copy_job_counts_x=load_data_source_file(
            working_folder / "Copy_Job_Counts_by_Product_Type.xlsx"
        ),
        mo_accuracy_x=load_data_source_file(
            working_folder / "Monthly_Management_Accuracy.xlsx"
        ),
        mo_timeliness_x=load_data_source_file(
            working_folder / "Monthly_Management_Timeliness.xlsx"
        ),
        log_file_p=app_files / "MOR_Log.txt",
    )
