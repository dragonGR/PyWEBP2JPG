# PyWEBP2JPG

This script batch converts all .webp files in a specified directory to .jpg format. The results are saved in a `\converted` subdirectory inside the source folder.

## Requirements
- Python 3.7+
- Pillow (`pip install Pillow`)

## Usage
1. Install dependencies:
   ```powershell
   pip install Pillow
   ```
2. Run the script, specifying the path to the directory with .webp files. Optionally, you can specify JPG quality (0-95, default is 85):
   ```powershell
   python main.py path\to\your\directory [quality]
   ```

3. All converted .jpg files will be saved in the `\converted` folder inside the specified directory.

## Notes
- If the `\converted` folder does not exist, it will be created automatically.
