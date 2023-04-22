#! python3

# westCentralData.py - collects daily readings of data from West Central Website (Ulen)

import requests
import bs4
import openpyxl
import datetime
# Get website data as html, parse, and create dictionary of data to use for updating spreadsheet
res = requests.get('https://www.westcentralag.com/grain/cash-bids-futures')
res.raise_for_status()

onlyTable = bs4.SoupStrainer("tbody > tr > td > table > tbody > tr:nth-child(1) > td > table.DataGrid.DataGridPlus.DataNormal > tbody:nth-child(3) > tr > td:nth-child(1)")
# Use beautiful soup to parse HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser', parse_only=onlyTable)
#dtn-bids > tbody > tr > td > table > tbody > tr:nth-child(1)
#dtn-bids > tbody > tr > td > table > tbody > tr:nth-child(5)
#dtn-bids > tbody > tr > td > table > tbody > tr:nth-child(9)
for string in soup.strings:
    print(repr(string))
'''
commoditiesList = soup.find_all('b')
commoditiesDict = {}
for item in commoditiesList:
    commoditiesDict[str(item.text.strip())] = {}
print(commoditiesDict)

datesUnderCommodity = soup.select("table > colgroup > thead > tbody > tr > td")
for date in datesUnderCommodity:
    commoditiesDict['CORN'][date.string] = {}

for string in soup.strings:
    print(repr(string))


#print(i, date)

    commoditiesDict[commodity][date] = {\
    'Data Collected - Date': datetime.date,
    'Delivery Date': dataSoup.select(#),
    'Futures Price': dataSoup.select(#),
    'Futures Month': dataSoup.select(#),
    'Basis': dataSoup.select(#),
    'Cash Price': dataSoup.select(#),
    'Futures Change': dataSoup.select(#)}

'''

'''
# Open and edit spreadsheet using new data
with openpyxl.Workbook(westCentralData.xlsx) as wb:
    for commodity in commodities:
        sheet = wb[commodity]
        for column in columns: #not syntactically correct
            columnName, maxRow = commodiatiesDict[commodity][columnName]



# Close spreadsheet, close browser
'''
