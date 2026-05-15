# Section 1
- Assignments for CS3030

## Installing venv
- run the command `python3 -m venv .venv`
- activate venv with `source .venv/bin/activate` (or `source .venv/bin/activate.fish` if using fish).

## Installing other dependencies from requirements.txt
- run the command `pip install requests`

## files_in_folder.py
- A practice script that reads the names of every file in the files_in_folder using python.

## renamer.py
- Renames every file in the folder by adding incremental numbering to the end of the titles using python.

## Sentinel
- A script that checks if the directory "insert directory here" exists.
- Navigate to the folder containing the file
- Type `./sentinel`
- If that does not work, you may need to type `chmod +x sentinel` first.

## Alias
- I recommend creating an alias for activating venv
- Navigate to .bashrc and create a new line using `alias work="cd ~/PATH-TO/swiss-army-knife-[NAME]/section1 && source .venv/bin/activate"`
