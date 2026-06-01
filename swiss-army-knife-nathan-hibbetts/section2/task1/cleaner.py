import pathlib

target_directory = '.'
target_files = pathlib.Path(target_directory).rglob("*.tmp")
for fileName in target_files:
    print("Found junk: " + str(fileName.resolve()))