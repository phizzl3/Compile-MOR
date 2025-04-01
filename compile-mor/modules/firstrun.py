"""
This module contains functions related to the first run of the program.
"""


def display_first_run_message(file_path: str) -> None:
    """
    Displays a message to the user with instructions for the first run of the program.
    Prompts the user to press Enter to exit the program.
    """
    print(
        f"""
        
    Welcome! It looks like this is the first time you've run the program.
    Please follow the steps below to get started:
    
    1. Copy the 'MOR_Numbers.xlsx' file to the following directory:
    
      {file_path}
    
    2. Open the Data Entry tab of the 'MOR_Numbers.xlsx' file and update the 
    number of RIOCH devices and Non-Networked Devices. Then update the cells 
    containing the names and total meter types for each device under Production 
    Info, making sure to match the names added to the 'config.json' file.
    
    3. A 'config.json' file has been created in the same directory as above with 
    some default data. Update the 'config.json' file with your specific information, 
    change "using default values" to false, and save it.
    
    4. After updating the files, run the program again. (Review the log file
    saved to the same directory to verify your cell names match the output.)
    """
    )

    input("    Press Enter to exit the program...")
    exit()


if __name__ == "__main__":
    display_first_run_message("/path/to/your/folder")
