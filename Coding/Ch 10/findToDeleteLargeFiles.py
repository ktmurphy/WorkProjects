#! python3
# findToDeleteLargeFiles.py - goes through files on computer and finds largest files, adds them to list and returns list

# This program will need to:
# from home directory, walk through all files and add to a list if they are certain size. Return list

import os
from pathlib import Path
p = Path.cwd()
bigFiles = []
for file in os.listdir(str(p)):
    if os.path.getsize(file) > 1000:
        bigFiles.append(file)

print(bigFiles)
