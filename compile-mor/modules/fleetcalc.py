import re
from pathlib import Path

import pdfplumber


def _get_totals_from_user() -> tuple[int, int]:
    """
    Prompt the user to manually enter the fleet totals for black & white and color volumes.

    Returns:
        tuple[int, int]: A tuple containing the black & white volume and color volume.
    """
    print(" Error getting fleet totals. Please enter them below.")
    while True:
        try:
            bw_volume = int(input(" Fleet Black & White Total: "))
            color_volume = int(input(" Fleet Color Total: "))
            return bw_volume, color_volume
        except ValueError:
            print(" Try again. Numbers only.")


def _read_text_from_pdf(pdf_path: Path) -> str | None:
    """
    Extract text from the first page of a PDF file.

    Args:
        pdf_path (Path): The path to the PDF file.

    Returns:
        str | None: The extracted text from the first page of the PDF, or None if an error occurs.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            page1 = pdf.pages[0]
            return page1.extract_text()
    except IOError:
        print(" Unable to get info from Executive Summary PDF...")
        return None


def _get_volumes_from_text(
    page_text: str, bw_regex: str, color_regex: str
) -> list[int, int]:
    """
    Extract the black & white and color volumes from the given text using regular expressions.

    Args:
        page_text (str): The text to search for volumes.
        bw_regex (str): The regular expression pattern for black & white volume.
        color_regex (str): The regular expression pattern for color volume.

    Returns:
        list[int, int]: A list containing the black & white volume and color volume.
    """
    comp_bw_regex = re.compile(bw_regex)
    comp_color_regex = re.compile(color_regex)
    try:
        bw_volume = comp_bw_regex.search(page_text).group(2).replace(",", "")
        color_volume = comp_color_regex.search(page_text).group(2).replace(",", "")
        bw_volume = int(bw_volume)
        color_volume = int(color_volume)
    except ValueError:
        bw_volume, color_volume = 0, 0
    return bw_volume, color_volume


def calculate_fleet_totals(
    exec_summary: Path, data: dict, bw_vol_regex: str, color_vol_regex: str
) -> None:
    """
    Calculate and update the total volumes for fleet usage.

    Args:
        exec_summary (Path): The path to the executive summary PDF.
        data (dict): The dictionary to update with the fleet totals.
        bw_vol_regex (str): The regular expression pattern for black & white volume.
        color_vol_regex (str): The regular expression pattern for color volume.
    """
    print(' Gathering Fleet totals from "Executive summary.pdf"...', end="")

    bw_volume: int = 0
    color_volume: int = 0

    page_text = _read_text_from_pdf(exec_summary)

    if page_text:
        bw_volume, color_volume = _get_volumes_from_text(
            page_text=page_text,
            bw_regex=bw_vol_regex,
            color_regex=color_vol_regex,
        )

    if not any([bw_volume, color_volume]):
        bw_volume, color_volume = _get_totals_from_user()

    data["Fleet Black and White"] = bw_volume
    data["Fleet Color"] = color_volume
    print("Done.")
