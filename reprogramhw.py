import re

text= '''Abbate, Lynne Administrative Specialist	Housing - Central Office ACK-219 labbate@fgcu.edu (239) 590-1302 Abdel-Rahman, Leila	Resident Director	Housing - South Village	SV-EAGLE-1015
labdel@gmail.com (239) 590-1820
Abdo, Christopher	OPS High School Culinary Instr	School of Resort & Hospitality Mgt
cabdo@fgcu.edu
Abercrombie, Mary	Instructor I	Dept Marine & Ecological Sciences	MOD2-22
mabercrombie@fgcu.edu (239) 590-7187
Aboulnasr, Khaled	Chair, Associate Professor	Dept of Marketing	LH - 3345
kaboulna@fgcu.edu
(239) 590-7598'''



phoneNumRegex=re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))? # area code
(\s|-)                    # seperator
\d\d\d                    # first set of numbers  
-                         # seperator
\d\d\d\d                  # second set of numbers
(((ext(\.)?\s)|x)         # extension
(\d{2,5}))?)''',re.VERBOSE)

emailRegex=re.compile(r'''
                                # some.+thing@something.com
[a-zA-z0-9_.+]+                # name part
@                               # symbol @
[a-zA-z0-9_.+]+  # domain part
[^\.]''',re.VERBOSE)
#import pyperclip
#text=pyperclip.paste()
extractedPhone=phoneNumRegex.findall(text)
allphonenum=[]
for phonenum in extractedPhone:
    allphonenum.append(phonenum[0])
print(allphonenum)
extractedemail=emailRegex.findall(text)

print(extractedemail)
results="\n".join(allphonenum)+"\n"+"\n".join(extractedemail)
print(results)
