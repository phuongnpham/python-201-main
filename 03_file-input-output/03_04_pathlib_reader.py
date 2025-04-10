# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import json
import csv
from pathlib import Path

file_path = Path.cwd().joinpath("03_file-input-output/file-counter")
json_path = file_path.joinpath("filecounts.json")
csv_path = file_path.joinpath("filecount.csv")

with open(json_path,"r") as json_file:
    dict_contents = json.load(json_file)

with open(csv_path, "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(dict_contents.values())