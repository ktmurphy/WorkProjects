
#! python3
# backupToZip.py backs up an entire folder and it's contents into a zip folder whose name increments
# program will need to import modules needed
# program will need to figure out current zip name based on zip files in the folder
# program will need to create a new Zip file and open it in 'write'
# program will need to write folders and files, skipping former zip files
# program will need to close the zipfile

import zipfile, os
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
            formerZipBase = os.path.basename(folder) + '_'
            if filename.startswith(formerZipBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()
    print('Done.')
#backupToZip('xxxx')
