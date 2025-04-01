"""
This module initializes the submodules for the Compile-MOR project.

Submodules:
- display: Functions for displaying ASCII art and welcome messages.
- fileoutput: Functions for outputting Python code and writing output files.
- fleetcalc: Functions for calculating fleet totals.
- getfiles: Functions for retrieving file objects.
- loadfile: Functions for loading data source files.
- mailcalc: Functions for calculating mail totals.
- mpscalc: Functions for calculating MPS totals.
- prodcalc: Functions for calculating production totals.
- firstrun: Functions for handling first run messages.
"""

from .display import display_ascii_art, display_welcome_message
from .fileoutput import output_py, write_output_file
from .fleetcalc import calculate_fleet_totals
from .getfiles import get_file_objects
from .loadfile import load_data_source_file
from .mailcalc import calculate_mail_totals
from .mpscalc import calculate_mps_totals
from .prodcalc import calculate_production_totals
from .firstrun import display_first_run_message
