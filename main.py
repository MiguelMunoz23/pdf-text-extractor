"""
Author: Miguel Angel Muñoz Rizo
First Created: July 2nd, 2022

This python project extracts text from selected pdfs and puts them in an Excel file.
"""
import os
from tkinter import Tk, filedialog


def main():
    """
    TODO:
    - Extract text from file example and see how it is visualized.
    """
    # pointing root to Tk() to use it as Tk() in program.
    root = Tk()
    # Hides small tkinter window.
    root.withdraw()
    # Opened windows will be active. Above all windows despite selection.
    root.attributes('-topmost', True)
    # Returns opened path as str
    open_file = filedialog.askdirectory()
    print("Path: ", open_file)

    # Return the list of files and directories present in a specified directory path.
    list_files = os.listdir(open_file)
    print("List of files: ", list_files)


if __name__ == '__main__':
    main()
