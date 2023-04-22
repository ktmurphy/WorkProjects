# Write your code here :-)
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

heroRegex = re.compile(r'Tina Fey|Batman')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

batRegex = re.compile(r'(B|b)?at(man|mobile|copter|bat)')
mo2 = batRegex.search('The Batmobile lost a wheel')
print(mo2.group())

phoneNumRegex1 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex1.search('My number is 218-415-0118')
mo4 = phoneNumRegex1.search('My number is 415-0118')
print(mo3.group())
print(mo4.group())

#greedy with upper and lowercase ha's
greedyHaRegex = re.compile(r'((H|h)(a)){3,5}')
mo5 = greedyHaRegex.search('HahaHaHaHa')
print(mo5.group())

lazyHaRegex = re.compile(r'(Ha){3,5}?')
mo6 = lazyHaRegex.search('HaHaHaHaHa')
print(mo6.group())

noNewLineRegex = re.compile('.*')
mo7 = noNewLineRegex.search('To serve and protect.\nTo live and to die.')
print(mo7.group())

newLineRegex = re.compile('.*', re.DOTALL)
mo8 = newLineRegex.search('To serve and protect.\nTo live and to die.')
print(mo8.group())

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

agentNamesRegex= re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
