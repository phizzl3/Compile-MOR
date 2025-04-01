def display_ascii_art(version: str) -> None:
    """
    Display ASCII art with the given version number.

    Args:
        version (str): The version number to display in the ASCII art.
    """
    art = f"""
  V{version}
  ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗██╗     ███████╗    ███╗   ███╗ ██████╗ ██████╗ 
 ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝    ████╗ ████║██╔═══██╗██╔══██╗
 ██║     ██║   ██║██╔████╔██║██████╔╝██║██║     █████╗█████╗██╔████╔██║██║   ██║██████╔╝
 ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║██║     ██╔══╝╚════╝██║╚██╔╝██║██║   ██║██╔══██╗
 ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║███████╗███████╗    ██║ ╚═╝ ██║╚██████╔╝██║  ██║
  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                                                                :8r@nd0N       
"""
    print(art)


def display_welcome_message() -> None:
    """
    Display a welcome message with instructions for required files.
    """
    print(
        """
        Before continuing, make sure you have the following files from 
        the month you're reporting on) in your "Downloads" folder: 
        
        * (PaperCut) Reports>Executive Summary>Previous Month>PDF
        * (TRAC) Insights>Reports>Assets>Meter Reads Data Dump
        * (TRAC) Insights>Reports>Copy>Monthly Management Accuracy
        * (TRAC) Insights>Reports>Copy>Monthly Management Timeliness
        * (TRAC) Insights>Reports>Copy>Copy Job Counts By Product Type
        
        The following files don't have to be in your "Downloads" folder,
        but make sure you have them available to manually enter data:
        
        * (PS_Scans) /Counters_and_Waste/{Current Year}/{Most Recent Waste PDF}
        * (PS_Scans) /Mail_Logs/{Current Year}/{Most Recent Mail Log PDF}
        
        Verify you have these files and press ENTER to continue...
        """
    )


if __name__ == "__main__":
    display_ascii_art("12345")
    display_welcome_message()
