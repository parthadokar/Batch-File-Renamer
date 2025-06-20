import os
# import time
# import sys
import argparse

# Create a parser
parser = argparse.ArgumentParser(description='changes the start of the files')
# Add positional arguments: the first defines the directory path, the second defines the prefix to add
# 'metavar' changes how the argument is shown in the help/usage text.
# Specify the expected data type for each argument
# use the help function always to help the user understand what is to be inputed in the command line
parser.add_argument('dir_path',metavar='dir_path',type=str,help="enter the path you want to change files names")
parser.add_argument('start',metavar='start',type=str,help='enter what you want to replace it with')
# create args and create intance for the args
args = parser.parse_args()
dir_path = args.dir_path
start = args.start

def rename():
    # Specify the directory path
    path = dir_path

    # Loop through all files in the directory
    for filename in os.listdir(path):
        # Check if the file is a text file
        if filename.endswith(".json"):
            # Construct the old and new file paths
            old_file_path = os.path.join(path, filename)
            new_file_name = f"{start}_{filename}"
            new_file_path = os.path.join(path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_file_name}")

# def change_time():
#     # Specify the directory path
#     directory = dir_path
#     new_time = time.mktime(time.strptime("2025-08-20 12:00:00", "%Y-%m-%d %H:%M:%S"))

#     # Loop through all files in the directory
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         # Check if the file is a text file
#         if os.path.isfile(file_path):
#             # Modify the file
#             os.utime(file_path, (new_time, new_time))
#             print(f"Modified time for: {filename}")

# def run():
#     print("Welcome to Windows System Modifier\n")
#     choice = input("What would you like to do?\n1. Rename Files\n2. Change Time on Files\n")
    
#     if choice == "1":
#         rename()
#     elif choice == "2":
#         change_time()
#     else:
#         print("Invalid choice. Exiting...")
#         sys.exit()

if __name__ == '__main__':
    rename()