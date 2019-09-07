# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:43:30 2019

@author: My Pc
"""

import re

def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i  in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message="Call  me  415-555-2222 tomorrow ," \
        " or at 415-555-1111"
foundNumber=False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number exists",chunk)
        foundNumber=True
if not foundNumber:
        print("Could not find any number")

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search(message)
print(mo.group())
print(phoneNumRegex.findall(message))

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

message="Call  me  (415) 555-2222 tomorrow , or at (415) 555-1111"

phoneNumRegex=re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo=phoneNumRegex.search(message)
print(mo.group())

'''using pipe character'''

batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search("Batmobile lost a wheel")
print(mo.group())

'''to check which value found from regex'''

print(mo.group(1))

'''? to get the value 0 or one time '''
batRegex=re.compile(r'Bat(wo)?man')
mo=batRegex.search("Adventures of Batman")
print(mo.group())
mo=batRegex.search("Adventures of Batwoman")
print(mo.group())

mo=batRegex.search("Adventures of Batwowowowman")

print(mo==None)


phoneNumRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search("My phone number is 212-555-9999")
print(mo.group())
mo=phoneNumRegex.search("My phone number is 555-9999")
print(mo.group())

'''* means zero or more'''

batRegex=re.compile(r'Bat(wo)*man')
mo=batRegex.search("Adventures of Batwowowowowowoman")
print(mo.group())
mo=batRegex.search("Adventures of Batmanmanmanmanman")
print(mo.group())
 
''' ^ denotes starts with and $denotes end with'''
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.group())

'''' to find out location of first whitespace in given string'''

x = re.search("\s", "The rain in Spain")
print(x.start())

''' split function '''

x = re.split("\s", "The rain in Spain")
print(x)

x = re.split("\s", "The rain in Spain",2)
print("The one is ",x)

''' to find out the occurrence of Letter from start and end point'''
x = re.search(r"\bS\w+","The rain 123 in Spain Singapore")

'''span() used to find out the start and end index of resultant value from regex'''
print("Span= ",x.span())

'''return the complete string'''
print("String =",x.string)

''' resultant string as per regex used''' 
print(x.group())

NumRegex=re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
 
'''?  means zero or one * means zero or more and + means one or more '''

regex=re.compile(r'Bat(wo)?man')
print(regex.search("Adventures of Batwoman").group())
regex=re.compile(r'\*\+\?')
print(regex.search("I had learnt usage of *+? mark in python").group())
regex=re.compile(r'(\*\+\?)+')
print(regex.findall("I had learnt usage of *+? mark in python and usage of *+?"))
regex=re.compile(r'(HA){3}')
print(regex.search("He said HAHAHA").group())

phoneNumRegex=re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneNumRegex.search("My numbers are 212-564-9696,555-9678,859-967-8545").group())
print("Using findall ",phoneNumRegex.findall("My numbers are 212-564-9696,555-9678,859-967-8545"))

regex=re.compile(r'(HA){3,5}')
 
print(regex.search("He says HAHAHA").group())
print(regex.search("He says HAHAHAHAHA").group())
print(regex.search("He says HAHAHAHAHAHA").group())
regex=re.compile(r'(HA){,5}')
print(regex.search("He says HAHAHAHAHAHA").group())
regex=re.compile(r'(HA){3,}')
print(regex.search("He says HAHAHAHAHAHAHAHAHAHA").group())

'''regular expression by default perform greedy matches means search max longest possible string matches the pattern'''
regex=re.compile(r'(\d){3,5}')
print(regex.search("1234567879").group())


''' to perform non-greedy match we mention ? mark at the end of pattern for eg (r'(\d){3,5}?) and non-greedy match looks for smallest possible string'''


regex=re.compile(r'(\d){3,5}?')
print(regex.search("12345678790").group())

phoneRegEx=re.compile(r'\d\d\d \d\d\d \d\d\d\d')
print(phoneRegEx.search("My number is 965 000 8989 and 965 898 7856").group())
print(phoneRegEx.findall("My number is 965 000 8989 and 965 898 7856"))     

phoneRegEx=re.compile(r'((\d\d\d) (\d\d\d \d\d\d\d))')
print("Value findall ",phoneRegEx.findall("My number is 965 000 8989 and 965 898 7856"))
l=phoneRegEx.findall("My number is 965 000 8989 and 965 898 7856")
print(l[0][2])
#print(phoneRegEx.search("My number is 965 000 8989 and 965 898 7856").group())

digitRegex=re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
print(digitRegex.findall("Thi is sample 1 2 3 4 with sample 9 8 4"))

digitRegex=re.compile(r'(\d)')
print(digitRegex.findall("Thi is sample 1 2 3 4 with sample 9 8 4"))
lyrics='''On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree


 

On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''

''' regular expression to find number with some characters'''
xmasRegex=re.compile(r'\d+\s+\w+')
print(xmasRegex.findall(lyrics))
vowelRegex=re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall("This is created to test vowel appearanve in given string India"))
consonantRegex=re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall("This is created to test vowel appearanve in given string India"))

''' to get th matching string that contains only special characters'''
spcharRegex=re.compile(r'[^A-Za-z0-9]')
print(spcharRegex.findall(" This is Ankit @#@$#@!$@#$@#!% Hi this "))

''' to get th matching string that contains only alphabets and numbers and excludes special character'''

spcharRegex=re.compile(r'[A-Za-z0-9]')
print(spcharRegex.findall(" This is Ankit @#@$#@!$@#$@#!% Hi this  89 "))

''' to get th matching string that contains only alphabets   and excludes numbers and special character'''
spcharRegex=re.compile(r'[A-Za-z]')
print(spcharRegex.findall(" This is Ankit @#@$#@!$@#$@#!% Hi this  89 "))

''' to get th matching string that contains only numbers   and excludes  alphabets and special character'''
spcharRegex=re.compile(r'[0-9]')
print(spcharRegex.findall(" This is Ankit @#@$#@!$@#$@#!% Hi this  89 "))

''' ^ to creat regex and check the given String should starts with regex given'''
beginsWithHelloRegex=re.compile(r'^Hello')
print(beginsWithHelloRegex.search("Hello this is World").group())

''' $ to creat regex and check the given String should ends  with regex given'''

endsWithWorldRegex=re.compile(r'World!$')
print(endsWithWorldRegex.search("Hello World!").group())

'''regex too make sure that entire string is a digit '''

allDigitsRegex=re.compile(r'^\d+$')
print(allDigitsRegex.findall("12348910"))

''' .(dot) anything after one character following at given in regex except new line '''

dotRegex=re.compile(r'.at')
print(dotRegex.findall("The ccat is sat on flat mat mature brat "))

''' .(dot) means complete string that has sub 
string in regex  from the bginning to the sub string given in regex 
when used {1,2} value as start and second char'''

dotRegex=re.compile(r'.{1,2}at')
print("This is with . operator"+str(dotRegex.findall("The cat is sat on flat mat mature brat ")))

'''.* any pattern whatsoever'''

Name="First Name: Ankit Last Name: Mittal"
print(Name.find(":")+2)
print(Name[18:])
NameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
print(NameRegex.findall(Name))

'''non-greedy pattern'''

NonGreedy=re.compile(r'<(.*?)>')
print(NonGreedy.findall( "<To serve Humans> for dinner.>" ))


'''greedy pattern'''

NonGreedy=re.compile(r'<(.*)>')
print(NonGreedy.findall( "<To serve Humans> for dinner.>" ))

prime="Serve public trust.\nProtect the innocent.\nUphold the law"
print(prime)
dotstarRegEx=re.compile(r'.*')
print("Thi is with single line . operator",dotstarRegEx.search(prime).group())
dotstarRegEx=re.compile(r'.*',re.DOTALL)
print("With DOTALL operator",dotstarRegEx.search(prime).group())

''' to create regex for lowercase and upper case both use re.IGNORECASE or re.I'''
vowelRegex=re.compile(r'[aeiou]',re.IGNORECASE)
print(vowelRegex.findall("This is created to test vowel appearanve in given string INDIA"))

''' sub method'''
''' \w+ will find the next set of character till the time time didnt find the character'''

namesRegEx=re.compile(r'Agent \w+')
print(namesRegEx.findall("Agent Alice gave the script to Agent Bob"))

''' sub method finds the occurrence of String u passes also repalce ith with String given in Sub method '''

print(namesRegEx.sub("REDACTED","Agent Alice gave the script to Agent bob"))

namesRegEx=re.compile(r'Agent (\w)(\w)\w*')

print(namesRegEx.findall("Agent AliceMiller  gave the script to Agent Bob"))

''' \1 indicates first group and \2 indicates second gorup and so on as per regex given '''
print(namesRegEx.sub(r"Agent \1*****","Agent Alice gave the script to Agent Bob"))

'''Verbose make regesx more readable'''
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
text="This is sample text with some phone numbers i.e 212-963-7894 or (212) 968-9675 or 555-0000 and email ankit.mittal@lendkey.com or ankitkrmittal25@gmail.com."
extractedPhone=phoneNumRegex.findall(text)
allphonenum=[]
for phonenum in extractedPhone:
    allphonenum.append(phonenum[0])
print(allphonenum)
extractedemail=emailRegex.findall(text)

print(extractedemail)
results="\n".join(allphonenum)+"\n"+"\n".join(extractedemail)
print(results)



