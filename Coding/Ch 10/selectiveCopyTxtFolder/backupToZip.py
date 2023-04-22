
#! python3
# backupToZip.py backs up an entire folder and it's contents into a zip folder whose name increments

import zipfile, os
from pathlib import Path
def backupToZip(folder):
    #ensure folder is absolute path
    folder = os.path.abspath(folder)
    #figure out which file name should be used based on which ones already exist
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    #create zip file
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, filenames in os.walk(folder):

        print(f'Adding files in {foldername}...')
        #add the current folder to the zip file
        backupZip.write(foldername)

        #add all the files in this folder to zip file
        for filename in filenames:
            #don't back up zip files
            newBase = os.path.basename(folder) + '-'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()
    print('Done.')
backupToZip(str(Path.cwd()))
