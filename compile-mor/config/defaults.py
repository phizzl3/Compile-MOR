"""
This module contains the default configuration settings for the Compile-MOR application.
These settings include options for logging, output file handling, regex patterns for volume
detection, and machine-specific information such as rates and serial numbers.
"""

DEFAULTS = {
    "using default values": True,
    "write log file": True,
    "open output file": True,
    "grayscale volume regex": "(Grayscale:\\s)((\\d{1,3},)?(\\d{1,3},)?(\\d{1,3}))",
    "color volume regex": "(Color:\\s)((\\d{1,3},)?(\\d{1,3},)?(\\d{1,3}))",
    "production info": {
        "bw machine 1": {
            "name": "BW1",
            "serial number": "00000000000",
        },
        "bw machine 2": {
            "name": "BW2",
            "serial number": "00000000000",
        },
        "color machine 1": {
            "name": "CLR1",
            "serial number": "00000000000",
        },
        "color machine 2": {
            "name": "CLR2",
            "serial number": "00000000000",
        },
        "meter columns": {
            "serials": "P",
            "total black and white": "BF",
            "total color": "BK",
        },
    },
}
"""Default values for program."""
