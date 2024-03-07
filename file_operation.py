import os
import shutil
from datetime import datetime, timedelta

def list_files_in_directory(directory):
    """List all files in the given directory."""
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def is_recently_modified(file_path, hours=24):
    """Check if a file has been modified or created in the last 'hours' hours."""
    current_time = datetime.now()
    file_stat = os.stat(file_path)
    
    # Consider both modification time and creation time
    modified_time = datetime.fromtimestamp(file_stat.st_mtime)
    created_time = datetime.fromtimestamp(file_stat.st_ctime)
    
    time_difference_modified = current_time - modified_time
    time_difference_created = current_time - created_time
    
    return time_difference_modified <= timedelta(hours=hours) or time_difference_created <= timedelta(hours=hours)

def update_file(file_path):
    """Update the content of a file, for example, by appending a timestamp."""
    with open(file_path, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\nUpdated at {timestamp}")

def create_last_24hours_folder(folder_name):
    """Create a folder if it does not exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_file_to_folder(source, destination):
    """Move a file from the source directory to the destination directory."""
    shutil.move(source, destination)

def main():
    current_directory = os.getcwd()
    last_24hours_folder = "last_24hours"
    
    create_last_24hours_folder(last_24hours_folder)
    
    files_to_update_and_move = [
        file for file in list_files_in_directory(current_directory)
        if is_recently_modified(os.path.join(current_directory, file))
    ]
    
    if not files_to_update_and_move:
        print("No files found within the last 24 hours.")
    else:
        print("Files to be updated and moved:")
        for file_name in files_to_update_and_move:
            file_path = os.path.join(current_directory, file_name)
            
            # Update the file content
            update_file(file_path)
            
            # Move the file to the "last_24hours" folder using shutil.copy2 for preserving metadata
            destination_path = os.path.join(current_directory, last_24hours_folder, file_name)
            move_file_to_folder(file_path, destination_path)
            
            print(f"Updated and moved: {file_name} to {destination_path}")

if __name__ == "__main__":
    main()
