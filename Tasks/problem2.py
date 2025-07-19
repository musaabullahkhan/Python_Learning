import os

# Get the directory you want to list (current directory in this case)
directory_path = '.'  # You can also use any specific path like 'C:/Users/YourName/Documents'

# Use os.listdir() to get all files and folders in the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
