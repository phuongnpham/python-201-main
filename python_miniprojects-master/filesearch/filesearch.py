from pathlib import Path

folder_path = Path.home().joinpath("Downloads")
jpg_files = []

for level1 in folder_path.iterdir():
    if level1.is_dir():
        for level2 in level1.iterdir():
            if level2.suffix == ".jpg":
                jpg_files.append(level2.resolve())
    else:
        if level1.suffix == ".jpg":
            jpg_files.append(level1.resolve())

for file in jpg_files:
    print(file)

