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

for extenstion, count in file_type.items():
    if count >= 5:
        folder_name = f"{extension}"
        folder_path = desktop.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)

        for f in desktop.iterdir():
            if f.suffix == extension:
                destination = folder_path.joinpath(f.name)
                f.replace(destination)
