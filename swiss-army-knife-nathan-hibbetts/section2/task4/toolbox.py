import argparse, pathlib

parser = argparse.ArgumentParser()
parser.add_argument('--path',help='The path of the folder'
                                  ' you wish to search in', required=True) #Location to search in
parser.add_argument('--ext', help='The file type to search for.'
                                  ' Do NOT include the period.', required=True) #File extention to search for
args = parser.parse_args()

target_directory = args.path
target_files = pathlib.Path(target_directory).rglob(f"*.{args.ext}")
for fileName in target_files:
    print("Found junk: " + str(fileName.resolve()))

