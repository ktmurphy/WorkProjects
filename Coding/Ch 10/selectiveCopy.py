#! python3
# selective copy copies only text files to another folder

# This program will need to find file names that are txt
# walk through directory and copy to new folder
# will need the following modules: re, os, from pathlib import path, shutil
# create regex for folder name or use glob
# 1. take a folder name and get absolute path of the folder
# 2 Create a folder for copied files in the same directory titled "folder_txtFilesOnly"
# 2 use walk to walk through tree
# 3 use glob to find folders
# copy those to new folder

#import modules
import shutil, os, re
from pathlib import Path
#regex for searching
filePattern = re.compile(r'^(.*)?\.txt')

#create folder if it doesn't exist for folders. Folder name: "selectiveCopy_parentfoldername"
# Folder location: Parent Folder, so both copy and actual folder are in same place but separate

# get path of current folder as string
p = Path.cwd()

# get parent folder
parent = p.parent.absolute()

#get copied folder path based on parent folder
copiedFolderPath = parent / Path('selectiveCopy_' + p.name)


if not copiedFolderPath.exists():
    copiedFolderPath.mkdir()

for folderName, subfolders, filenames in os.walk(p):
    for filename in filenames:
        isTxtFile = filePattern.search(filename)

        if isTxtFile == None:
            continue

        shutil.copy((p / filename), (copiedFolderPath))


