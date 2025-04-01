# Compile MOR

Compiles MOR info for monthly reports.

## Features

* Opens `Meter_Reads_Data_Dump.xlsx` from the Downloads folder if found. Asks for it via drag-and-drop if not. Reads Production totals from the file.
* Opens Monthly Accuracy, Timeliness, and Copy Jobs reports from the Downloads folder if found. Reads data from the file. If not found, asks for totals via user input.
* Opens `Executive Summary.pdf` from the Downloads folder if found. Asks for it via drag-and-drop if not. Reads Fleet totals from the file.
* Reads previous month's MPS data from `MOR_Numbers.xlsx` and asks if any machines have been added or moved. Updates totals based on user response.
* Gets all mail volumes via user input.
* Combines all totals and outputs data to `MOR_Numbers.xlsx` file located in the application's PyAppFiles folder.
* Optionally outputs a log file with combined totals.
* Optionally opens `MOR_Numbers.xlsx` file.

## Build Information

### Windows

```bash
pyinstaller -F --icon=.\icon\mor.ico -n "Compile MOR" .\compile-mor\main.py
```

### MacOS

```bash
pyinstaller -F -n "Compile MOR" ./compile-mor/main.py
```

Apply icon in MacOS Finder after compiling binary.
