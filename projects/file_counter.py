# Add the code for the file counter script that you wrote in the course.
import pprint
from pathlib import Path

desktop = Path().home().joinpath("Desktop")
file_type = {}

for f in desktop.iterdir():
    if f.is_file():
        if f.suffix:
            extension = f.suffix.lower()
        else:
            extension = "no extension"

        if extension in file_type:
            file_type[extension] += 1
        else:
            file_type[extension] = 1

print("File types on the Desktop:")
pprint.pprint(file_type)