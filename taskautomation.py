import os

def rename_files(directory, suffix):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    # Iterate over each file in the directory
    for file_name in file_list:
        # Check if the file ends with the given suffix
        if file_name.endswith(suffix):
            # Generate the new file name by adding a prefix to the original name
            new_file_name = f"new_{file_name}"
            
            # Get the full path of the original file and the new file
            old_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)

    print("Files renamed successfully!")

# Usage example
directory = "/path/to/directory"  # Update with your directory path
suffix = ".txt"  # Update with your desired file suffix
rename_files(directory, suffix)