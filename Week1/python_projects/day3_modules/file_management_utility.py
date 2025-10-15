import os
import random
from colorama import init, Fore, Back, Style

init()

def sanitize_path(user_path: str) -> str:
    p = user_path.strip().strip('"').strip("'")
    p = os.path.expanduser(p)
    p = os.path.abspath(p)
    return p

def convert_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} Bytes"
    elif size_bytes < 1024**2:
        return f"{size_bytes/1024:.2f} KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes/(1024*1024):.2f} MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.2f} GB"

def valid_Number_Error():
    print(Fore.RED + "Please Enter a valid number. " + Style.RESET_ALL)

def File_Exists_Error():
    print(Fore.YELLOW + "File already exists !" + Style.RESET_ALL)

def Permission_Error():
    print(Fore.RED + "Permission Denied!" + Style.RESET_ALL)

def list_files(folder):
    try:
        folder = sanitize_path(folder)
        files = os.listdir(folder)
        return files
    except(PermissionError):
       Permission_Error()
    except(NotADirectoryError):
        print(Fore.RED + "The specified path is not a directory!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error : " + str(e) + Style.RESET_ALL)

def pick_random_file(files):
    try:
        file = random.choice(files)
        return file
    except(PermissionError):
        Permission_Error()
    except Exception as e:
        print(Fore.RED + "Error : " + str(e) + Style.RESET_ALL)

def show_file_details(folder, file):
    try:
        file_path = os.path.join(folder, file)
        print(Fore.CYAN + "File name: " + Style.RESET_ALL + Fore.WHITE + f"{file}" + Style.RESET_ALL)
        print(Fore.CYAN + "Full path: " + Style.RESET_ALL + Fore.WHITE + f"{os.path.abspath(file_path)}" + Style.RESET_ALL)
        size_bytes = os.path.getsize(file_path)
        print(Fore.CYAN + "File size: " + Style.RESET_ALL + Fore.WHITE + f"{convert_size(size_bytes)}" + Style.RESET_ALL)
    except PermissionError:
        Permission_Error()
    except FileNotFoundError:
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)

def createfile():
    try:
        number_of_file=int(input("How many files you Want to create :"))
        base_name = input(Fore.CYAN + "Enter the base name for the files (e.g., 'document'): ")
        extension = input(Fore.CYAN + "Enter the file extension (e.g., 'log'): ")
        for i in range(number_of_file):
            filename = f"{base_name}{i}.{extension}"
            try:
                with open (filename,"x"):
                    pass
                print(Fore.GREEN+f"New file created : {filename}"+Style.RESET_ALL)
            except(FileExistsError):
                File_Exists_Error()
            except(PermissionError):
                Permission_Error()
    except(ValueError):
        valid_Number_Error()

def removeFixedFiles():
    folder = input("Enter folder path: ")
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(Fore.RED + "Folder not found!" + Style.RESET_ALL)
        exit()
    except NotADirectoryError:
        print(Fore.RED + "The specified path is not a directory!" + Style.RESET_ALL)
        exit()
    except PermissionError:
        Permission_Error()

    try:
        start_pattern=""
        end_pattern=""
        option=0
        try:
            option = int(input("What You Want To Do ? \n1. Delete files that START with a particular name \n2. Delete files that END with a particular name \nPlease type 1 or 2 : "))
        except(ValueError):
            valid_Number_Error()
        if option != 1 and option != 2:
            print(Fore.RED + "invalid input!" + Style.RESET_ALL)
            pass
        elif option == 1:
            start_pattern = input("Please Enter The First name of file : ")
        elif option ==2:
            end_pattern = input("Please Enter The Last name of file : ")
        matching_files = []
        for file in files:
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path) and (file.startswith(start_pattern) or file.endswith(end_pattern)):
                matching_files.append(file)
        if not matching_files:
            print(Fore.YELLOW + "No files matched the given patterns." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "\nThe following files will be deleted:" + Style.RESET_ALL)
            for f in matching_files:
                print(Fore.CYAN + f + Style.RESET_ALL)
            confirm = input("\nType 'YES' to confirm deletion: ")

            if confirm.upper() == "YES":
                for file in matching_files:
                    try:
                        os.remove(os.path.join(folder, file))
                        print(Fore.GREEN + f"Deleted: {file}" + Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED + f"Could not delete {file}: {e}" + Style.RESET_ALL)
                print(Fore.GREEN + "\nDeletion completed!" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "\nDeletion cancelled." + Style.RESET_ALL)
    except Exception as e :
        print(Fore.RED + str(e) + Style.RESET_ALL)

def show_random_file():
    folder_path = sanitize_path(input("Enter Your Folder path: "))

    files = list_files(folder_path)
    if not files:
        print(Fore.YELLOW + "No files found in this folder." + Style.RESET_ALL)
        return
    random_file = pick_random_file(files)
    print(Fore.CYAN + "\nRandomly selected file:" + Style.RESET_ALL)
    show_file_details(folder_path,random_file)

def show_menu():
    print(Fore.CYAN + "\n--- File Management Utility ---")
    print(Fore.YELLOW + "1. Create New Files")
    print(Fore.YELLOW + "2. Remove Files by Name Pattern")
    print(Fore.YELLOW + "3. Get Details of a Random File")
    print(Fore.YELLOW + "4. Exit")
    return input(Fore.CYAN + "Please choose an option (1-4): ")

def main_loop():
    while True:
        choice = show_menu()
        if choice == '1':
            createfile()
        elif choice == '2':
            removeFixedFiles()
        elif choice == '3':
            show_random_file()
        elif choice == '4':
            print(Fore.GREEN + "Exiting. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option, please try again.")

if __name__ == "__main__":
    main_loop()
