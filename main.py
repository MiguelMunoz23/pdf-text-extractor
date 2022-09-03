"""
Author: Miguel Angel Muñoz Rizo
First Created: July 2nd, 2022

This python project extracts text from selected pdfs and puts them in an Excel file.
"""
import os
from tkinter import Tk, filedialog
import PyPDF2
from easygui import multchoicebox


def select_directory():
    """
    This function shows a window to select folder with pdf files.

    @return: A list of the files found in the folder.
    """
    # Pointing root to Tk() to use it as Tk() in program.
    root = Tk()
    # Hides small tkinter window.
    root.withdraw()
    # Opened windows will be active. Above all windows despite selection.
    root.attributes('-topmost', True)
    # Returns opened path as str
    path = filedialog.askdirectory()
    print("Path: ", path)

    # Return the list of files and directories present in a specified directory path.
    list_files = os.listdir(path)
    print("List of files: ", list_files)

    # Add full route to each file
    for file in range(len(list_files)):
        list_files[file] = path + "/" + list_files[file]

    return list_files


def extract_text():
    """
    This functions extracts the text from the file.

    @return: A string with all the text from the file.
    """
    # Create a pdf file object
    pdf_file_obj = open('/home/miguel/PycharmProjects/pdf-text-extractor/pdf-files/pdf-example.pdf', 'rb')

    # Create a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Create a page object (get first page)
    page_obj = pdf_reader.getPage(0)

    # Extract text from first page
    text = page_obj.extractText()

    # Close the pdf file object
    pdf_file_obj.close()

    return text


def gui_options(choices):
    """
    This function creates a multiple choice box so the user can select all the choices that apply.
    @param choices: A python list of strings with the choices that are going to appear in the box.
    @return: A list of strings of all the selected choices.
    """
    text = "Select the required information"
    title = "Required Information"
    output = multchoicebox(text, title, choices)

    return output


def get_info(text, start_string):
    """
    This function extracts the selected information from the file.

    @param text: A string with all the text in the file.
    @param start_string: A string to look for in the text.
    @return: A string with the information requested.
    """
    # Get the start and end indices of where the desired string is defined
    start_indice = text.find(start_string)
    finish_indice = text.find("\n", start_indice)

    # Just get the text after ":" until newline "\n" and eliminate blank spaces
    info = text[start_indice:finish_indice].rsplit(":")[1].lstrip()

    return info


def main():
    # Get string of all the pdf file
    text = extract_text()
    # print(text)

    # Define the choices for the required information and let the user select all that apply
    # Nombre, calle y número, colonia, código postal
    choices = ["Name", "RFC", "Status"]
    required = gui_options(choices)
    print(f"Required info: {required}")

    # TODO: Prompt para seleccionar celdas de excel a donde se exportarán los datos

    info = list()
    for issue in required:
        if issue == "Name":
            info.append(get_info(text, "RazónSocial"))
        elif issue == "RFC":
            info.append(get_info(text, "RFC"))
        elif issue == "Status":
            info.append(get_info(text, "padrón"))

    print(f"Info retrieved: {info}")

    # info_dict = dict()
    # info_dict.keys = choices
    # info_dict.values = info
    # print(info_dict)

    # TODO: Tal vez trabajar con diccionarios? https://realpython.com/iterate-through-dictionary-python/


if __name__ == '__main__':
    main()
