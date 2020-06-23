# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:35:36 2019

@author: We-z
"""

import csv

def doprocess(sIn):
    s = [x.lower() for x in sIn]
    s = sorted(s)
    collect = {}
    for i in s:
        collect[i] = collect.get(i,0) + 1
    
    print (collect)  
    print ("")
    with open('wordlist.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(collect.items())
	
    writeFile.close()
    
    #this code can let user choose what word to search
    tofind = input("Please enter the word to search for and get how much times it has been used: ")
    tofind = tofind.lower()
    
    #tofind = 'the'
    found = 0
    for keyss in collect.keys():
        if (keyss == tofind):
            print("The word '%s' occured %d times." %(keyss, collect[keyss]))
            print("The word '{}' occured {} times.\n" .format(keyss, collect[keyss]))
            found = 1
            break
    
    if found == 0:
        print("The word '{}' occured {} times.\n" .format(tofind, 0))
    
    
#The above code is the function to count the unique words and save the output in csv file. 

a = []
b = []
print("There are two text files available for this program to test.")
userin = input("Please enter 1 or 2: ")

if userin != '1' or userin != '2':
    print("The user input is invalid")

while (userin == '1') or (userin == '2') :
    if userin == '1':
        with open("text1.txt")as fi:
            contents = fi.read()
            a = contents.split()
        doprocess(a)
    elif userin == '2':
        with open("text1.txt")as fi:
            contents = fi.read()
            a = contents.split()
        with open("text2.txt")as fib:
            contentsb = fib.read()
            b = contentsb.split()  
        s = a + b
        doprocess(s)
    
    userin = input("enter althernative number to try the different option or enter 'done' to exit: ")
    userin = userin.lower()
    
    
    if userin == 'done':
        exit


