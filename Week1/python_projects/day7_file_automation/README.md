# File Date Renamer Script

## Description

This Python script renames all files (excluding directories) in a specified folder by prefixing their names with the current date in `YYYY-MM-DD` format. It skips directories, logs all actions (successes and failures) to a `log.txt` file in the target folder, and handles basic errors like invalid paths or permission issues.

## Requirements

- Python 3.x (uses standard libraries: `os` and `datetime`)

No additional dependencies required.

## Usage

1. Save the script as `rename_files.py` (or any name).
2. Run the script from the command line:
   ```
   python rename_files.py
   ```
3. When prompted, enter the full path to the folder containing the files you want to rename (e.g., `/path/to/your/folder` or `C:\Users\YourName\Documents\folder`).
4. The script will:
   - Verify the folder exists.
   - List the files for confirmation.
   - Rename files (e.g., `example.txt` becomes `2025-10-20_example.txt`).
   - Create/update `log.txt` in the folder with details of each operation.
5. Review the console output and `log.txt` for results.

### Example

**Input folder contents before:**
- `document.pdf`
- `image.jpg`
- `subdir/` (directory, skipped)

**After running (assuming date is 2025-10-20):**
- `2025-10-20_document.pdf`
- `2025-10-20_image.jpg`
- `subdir/` (unchanged)
- `log.txt`

**Sample log.txt content:**
```
Renamed: document.pdf -> 2025-10-20_document.pdf
Renamed: image.jpg -> 2025-10-20_image.jpg
Skipped directory: subdir
```

## Notes

- The script overwrites existing files with the same new name (if any), as `os.rename` handles this natively.
- Run in a backup or test folder first to avoid unintended changes.
- Paths with spaces or special characters are supported, but ensure the input path is correctly quoted if needed in your shell.
