import os
from datetime import datetime

# Input folder path
file_path = input("Enter the folder path you want to rename files in: ")

# Check if folder exists
if not os.path.exists(file_path):
    print("Folder not found! Please enter a valid path.")
    exit()

# List files in folder
try:
    files = os.listdir(file_path)
    print("Files in folder:", files)
except Exception as e:
    print(f"Error reading folder: {e}")
    exit()

# Get current date in YYYY-MM-DD format
now = datetime.now().strftime("%Y-%m-%d")

# Open log file in the same folder
log_file_path = os.path.join(file_path, "log.txt")

try:
    with open(log_file_path, "w") as log:
        for file in files:
            old_path = os.path.join(file_path, file)

            # Skip directories
            if os.path.isdir(old_path):
                log.write(f"Skipped directory: {file}\n")
                continue

            new_path = os.path.join(file_path, f"{now}_{file}")

            try:
                os.rename(old_path, new_path)
                log.write(f"Renamed: {file} -> {now}_{file}\n")
            except Exception as e:
                log.write(f"Failed to rename {file}: {e}\n")

except Exception as e:
    print(f"Error writing log file: {e}")
    exit()

print(f"Renaming done! Check log file: {log_file_path}")
