# ********** Duplicate Files Remover in a Directory By Nouman Akram ***********
import os

def directory_item_list(directory: str)-> list:
    '''
    Returns the List of all files in parameter Directory.
            Parameters:
                    directory (str): directory path         
            Returns:
                    list (list): list that contain all files names
    '''
    return sorted(os.listdir(directory))

def view_directory_file(directory: str) -> None:
    '''
    Print the all items in directory file.
            Parameters:
                    directory (str): directory path         
            Returns:
                    None
    '''
    directroy_files = directory_item_list(directory) # retruns list of files in directory
    

    if len(directroy_files) > 0: 
        print("\tFiles in Directory")
        #loop to show the items in directory
        for i in range(len(directroy_files)):
            print("\t-------------------------------")
            print(f"\t{i+1} ==> {directroy_files[i]}")
            print("\t-------------------------------")
    else:
        print("No Files in Directory")
        

def remove_duplicate_files(directory: str) -> None:
    '''
    Remove all Duplicate files in Directory.
            Parameters:
                    directory (str): directory path         
            Returns:
                    None
    '''
    files = directory_item_list(directory)
    
    duplicates = set() #set to add the uniques values
    
    for i in range(len(files)):
        
        # directory +"/"+ files[i] -> to concat the directory and list file name to get the exact file
        with open(directory +"/"+ files[i], 'r') as firstfile:
            firstcontains = firstfile.read()
            
            for j in range(i+1 , len(files)):
                with open(directory + "/" + files[j], 'r') as secondfile:
                    secondcontains = secondfile.read()
                    
                    if firstcontains == secondcontains: #check the first file contents with 2nd file contents
                        duplicates.add(files[j]) #add the name of file in sets
                        
    #True if duplicates length is greater than 0
    if duplicates:
        print()
        
        for item in duplicates:
            os.remove(directory + "/" + item)
            print("\t----------------------------------------")
            print(f"\tSuccessfully Removed \"{item}\" File")
            print("\t----------------------------------------")
    else:
        print("\n\t-------------------------------")
        print("\tNo Duplication is Found")
        print("\t-------------------------------")
        

if __name__ == '__main__':

    print("*"*80)
    print("\t\nWelcome to the Duplicate Files Remover Application by ArhamSoft\n")
    print("*"*80)

    while True:
        
        try: 
            directory_input = input("\nEnter the Directory In which you want to remove duplicate files or enter 0 to exit : ")
            
            if os.path.isdir(directory_input):
                print("You have entered in Directory: ")
                print("Enter 1 to Show Files : ")
                print("Enter 2 to Exit : ")
                choice = int(input())
                if choice == 1:
                    view_directory_file(directory_input)
                    while True:
                        duplicate_remover = input("\tDo you want to remove Duplication (Y/n) : ").casefold()
                        if duplicate_remover == 'y':
                            delfile = remove_duplicate_files(directory_input)
                            break
                        elif duplicate_remover == 'n':
                            print("Thanks for using the duplication application")
                            break
                        else:
                            print("Please enter the valid option")
                elif choice == 2:
                    print("Thanks for using the application")
                    break
                else:
                    print("Please enter the valid choice")
                    
            elif directory_input == '0':
                print("\nThanks for using the Application")
                break
                    
            else:
                print("Please enter the Valid Directory Path\n")
        
        except Exception as err:
            print("\n\nYou have Enter the unexpected input, Thanks for using the application")
            break   
    
    
