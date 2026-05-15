import os
from os import rename

count = 0
files = [f for f in os.listdir('.') if not f.startswith('.')]
print(f"I have renamed {len(files)} files in this directory:")
for file in files:
    newName = file.split('.')
    newNameCharacter = newName[0].__add__(str(count))
    newNameCharacter = newNameCharacter.__add__(".txt")
    rename(file, newNameCharacter)
    count += 1
