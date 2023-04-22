#! python3
# selective copy copies only text files to another folder

# This program will need to find file names that are txt
# walk through directory and copy to new folder
# will need the following modules: re, os, from pathlib import path, shutil
# create regex for
import re, shutil, os
from pathlib import Path

filePattern = re.compile(r'^(.*)?\.txt')



for foldername, subfolders, filenames in os.walk('C:\\Users\\KatieMurphy\\Documents\\Coding\\Ch 10'):
    print(f'Current folder is {foldername}...')
    shutil.copytree(foldername, 'C:\\Users\\KatieMurphy\\Documents\\Coding\\selectiveCopyTxtFolder')



