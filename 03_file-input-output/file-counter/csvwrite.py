# Write the file counts to a `.csv` file.
import json
import csv

with open(("03_file-input-output/file-counter/filecounts.json"), "r") as filecounts:
    dict_contents = json.load(filecounts)

with open(("03_file-input-output/file-counter/filecount.csv"), "w") as file_out:
    writer = csv.writer(file_out)
    writer.writerow(dict_contents.values())