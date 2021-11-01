import os
import hashlib
from tkinter import Tk, filedialog


class DuplicateRemover:

    """
    A class to Remove Duplication in Directory.

    ...

    Attributes
    ----------
    directory : str
        Selected file Directory

    Methods
    -------
    directory_item_list():
        return the sorted list of all files in directory
    view_directory_file():
        Show all the files in directory

    remove_duplicate_files():
        Remove all duplicate files in directory
    """

    def __init__(self, directory):
        self.directory = directory

    def directory_item_list(self) -> list:
        '''
        Returns the List of all files in parameter Directory.
                Parameters:
                        directory (str): directory path
                Returns:
                        list (list): list that contain all files names
        '''
        return sorted(os.listdir(self.directory))

    def view_directory_file(self) -> None:
        '''
        Print the all items in directory file.
                Parameters:
                        directory (str): directory path
                Returns:
                        None
        '''
        directroy_files = self.directory_item_list()  # retruns list of files in directory

        if len(directroy_files) > 0:
            print("\tFiles in Directory")
            # loop to show the items in directory
            for index, value in enumerate(directroy_files):
                print("\t-------------------------------")
                print(f"\t{index+1} ==> {value}")
                print("\t-------------------------------")
        else:
            print("No Files in Directory")

    def remove_duplicate_files(self) -> None:
        '''
        Remove all Duplicate files in Directory.
                Parameters:
                        directory (str): directory path
                Returns:
                        None
        '''
        files_list = self.directory_item_list()

        unique_files = dict()  # set to add the uniques values

        for file in files_list:

            file_name = os.path.join(self.directory, file)

            if os.path.isfile(file_name):

                file_hash = hashlib.md5(
                    open(file_name, 'rb').read()).hexdigest()

                if file_hash not in unique_files:
                    unique_files[file_hash] = file_name

                else:
                    os.remove(file_name)
                    print(f"Successfully Removed {file} File")

        if len(unique_files) == len(files_list):
            print("\n\t-------------------------------")
            print("\tNo Duplication is Found")
            print("\t-------------------------------")


if __name__ == '__main__':

    print("*"*80)
    print("\t\nWelcome to the Duplicate Files Remover Application by ArhamSoft\n")
    print("*"*80)

    while True:

        Tk().withdraw()
        try:
            FOLDER_SELECTED = filedialog.askdirectory()

            duplicate_file_remove_application = DuplicateRemover(
                FOLDER_SELECTED)

            if os.path.isdir(FOLDER_SELECTED):

                print("You have entered in Directory")
                print("Enter 1 to Show Files : ")
                print("Enter 2 to Exit : ")

                try:
                    choice = int(input())

                except (ValueError, TypeError) as err:
                    print(f"{err}, Please Input the valid choice")

                except EOFError as err:
                    print("f{err}, can't read this input please input again")

                if choice == 1:
                    duplicate_file_remove_application.view_directory_file()

                    duplicate_remover = input(
                        "\tDo you want to remove Duplication (Y/n) : ").casefold()

                    if duplicate_remover == 'y':
                        duplicate_file_remove_application.remove_duplicate_files()

                    elif duplicate_remover == 'n':
                        print("\nWe happy to show you all files..")
                        break

                    else:
                        print("\nPlease enter the valid option")

                elif choice == 2:
                    print("Thanks for using the application")
                    break

                else:
                    print("Please enter the valid choice")

            else:
                print("Please enter the valid Directory Path\n")
                break

        except TypeError:
            print(f"Thanks for using Duplication Remover Application")
            break
