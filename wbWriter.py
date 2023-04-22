#! python3

# wbWriter.py - writes whitebox notes
# usage: wbWriter topic i/a/c numBiosC

import sys, bs4, re, pyperclip
from datetime import datetime


projectTopic = sys.argv[1]
initAdditConsolid = sys.argv[2]
if len(sys.argv) == 4:
    ifConsolidNumOfBios = int(sys.argv[3])
if projectTopic == 'long':
    projectTopic = input("What is the project topic? ")
# data for greetings and other in-email content. To do: Move to shelve
greetings = {'Monday':'Hope you had a good weekend!', 'Tuesday': 'Happy Tuesday!', 'Wednesday': 'I hope you are having a great week!',\
'Thursday': 'Hope all is well.', 'Friday': 'Happy Friday!', 'Saturday': 'Hope all is well.', 'Sunday': 'Hope all is well.'}
bioSentences = {\
'Initial': {\
1:'Thanks for sending over your project on %s! Here is an initial expert for this project.', \
2:'Thanks for sending over your project on %s! Here are some initial experts for this project.', \
3:'Thanks for sending over your project on %s! Here is a list of initial experts for this project.'},\
'Additional': {\
1:'Below is an additional expert I think would be a great fit for your %s project!',\
2:'Below are some additional experts I think would be a great fit for your %s project!', \
3:'Below is a list of additional experts I think would be a great fit for your %s project!'}, \
'ConsolidatedAndBios': {\
1:"I\'m sending one more expert for your %s project, as well as a consolidated list of bios.", \
2:"I\'m sending two more experts for your %s project as well as a consolidated list of all experts below.", \
3:"I\'m sending a few more experts for your %s project, as well as a consolidated list of all experts below."}}
screeningResponseNotes = {\
1:"I\'ve included a quick summary here, but this expert\'s full screening response and bio are below.",\
2:"I\'ve provided a quick summary of each, but please scroll down to take a look at the screening responses and full bios.",\
3:"A quick summary of these experts is available here, but take a look at their full screening responses and bios below."}
preSummaryClosing = {\
1:"Let me know if you\'d like to set up a call with this expert!", \
2:"Please let me know if you\'d like to speak with one of these experts.", \
3:"If you are interested in setting up a call with any of these experts, please let me know!"}
# Based on date, choose a greeting.
greetingDate = datetime.now()
day = greetingDate.strftime('%A')


# User saves HTML from Presenting Experts Page and Opens File
htmlOfPresentingExpertsPage = open('wbWriter.html')

onlyBody = bs4.SoupStrainer("main")
# Use beautiful soup to parse HTML
soup = bs4.BeautifulSoup(htmlOfPresentingExpertsPage, 'html.parser', parse_only=onlyBody, from_encoding = 'quoted_printable')

emailSubject = soup.find(class_=re.compile('3D"to'))



analystNameRegex = re.compile(r'(\n)*([A-Z])(=\n)((\w)+)')
analystName = analystNameRegex.search(emailSubject.get_text())
analystNameStr = str(analystName.group(2) + analystName.group(4))

memberNotes = soup.findAll(class_=re.compile("member-note"))
# Create a list of items for the wb note, to later be joined with a new line.
wbNoteList = []
wbNoteList.append('Hi ' + analystNameStr +',')
if initAdditConsolid != 'i':
    wbNoteList.append(greetings[day])

# Assess quantity of bios
if not len(sys.argv) == 4:
    if len(memberNotes) > 3:
        quantity = 3
    else:
        quantity = len(memberNotes)
else:
    if ifConsolidNumOfBios > 3:
        quantity = 3
    else:
        quantity = ifConsolidNumOfBios

if initAdditConsolid == 'i':
    wbNoteList.append(bioSentences['Initial'][quantity] % projectTopic)
elif initAdditConsolid == 'a':
    wbNoteList.append(bioSentences['Additional'][quantity] % projectTopic)
elif initAdditConsolid == 'c':
    wbNoteList.append(bioSentences['ConsolidatedAndBios'][quantity] % projectTopic)
if len(memberNotes) == 1:
    wbNoteList.append(screeningResponseNotes[quantity])
elif len(memberNotes) == 2:
        wbNoteList.append(screeningResponseNotes[quantity])
elif len(memberNotes) >= 3:
        wbNoteList.append(screeningResponseNotes[quantity])

def processMemberNotes(memberNotes, length):
    for i in range(int(length)):
        editedNote = memberNotes[i].text
        editedNote = editedNote.translate( {ord(i): None for i in '='} )
        editedNote = editedNote.replace('\n', '')

        #Remove Colon, New Lines, and add periods
        colonRegex = re.compile(r':(\S)')
        editedNote = colonRegex.sub('. \g<1>', editedNote)
        periodRegex = re.compile(r'\.(\S)')
        editedNote = periodRegex.sub('. \g<1>', editedNote)
        letterRegex = re.compile(r'([a-z])([A-Z])')
        editedNote = letterRegex.sub('\g<1>. \g<2>', editedNote)
        mnRegex = re.compile(r'Member Note. ')
        editedNote = mnRegex.sub('', editedNote)

        if editedNote[-1] != '.':
            editedNote = editedNote + '.'

    #Add to list of pieces (insert)
        #print('\n', str(editedNote))
        wbNoteList.append(str(editedNote))

if initAdditConsolid == 'c':
    processMemberNotes(memberNotes, ifConsolidNumOfBios)
elif initAdditConsolid == 'i' or initAdditConsolid == 'a':
    processMemberNotes(memberNotes, len(memberNotes))




wbNoteList.append(preSummaryClosing[quantity])
wbNoteList.append('Thanks,\nKatie')
wbNote = '\n\n'.join(wbNoteList)

wbNoteList.append('Thanks,\nKatie')
pyperclip.copy(wbNote)
htmlOfPresentingExpertsPage.close()
print('White Box Note Is Ready')


