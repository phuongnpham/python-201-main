# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.
import csv
import pprint
from pathlib import Path

desktop = Path.home().joinpath("Desktop")
file_path = Path.cwd().joinpath("03_file-input-output")
csv_file_path = file_path.joinpath("desktop_file_counts.csv")
file_types = {
    ".txt": 0,
    ".jpg": 0,
    ".ini": 0,
    ".lnk": 0,
    "no extension": 0
}
for f in desktop.iterdir():
    if f.is_file():
        if f.suffix:
            extension = f.suffix.lower()
        else:
            extension = "no extension"

        if extension in file_types:
            file_types[extension] += 1
        else:
            file_types[extension] = 1

print("File types on the Desktop:")
pprint.pprint(file_types)

with open(csv_file_path, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Extension", "Count"])
    for extension, count in file_types.items():
        writer.writerow([extension, count])