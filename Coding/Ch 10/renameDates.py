#! python3
#renameDates.py goes through file names in current directory to find files with American dates MM-DD-YYYY and to rename those to european-style dates DD-MM-YYYY

import shutil, os, re

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    print(beforePart, monthPart, dayPart, yearPart, afterPart)

    euroFilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print(f'Renaming {amerFilename} to {euroFilename}...')
    #shutil.move(amerFilename, euroFilename)




