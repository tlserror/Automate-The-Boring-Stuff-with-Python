#!/usr/bin/python3 
# regexsearh.py based on the "regex search" assignment in chapter 8 of 
# Auotmate the Boring Stuff with Python.
# The script finds all .txt files in a directory it was run in and matches any context in those files 
# based on a user provided regex pass via a cli argument.
# 
# Usage: regexsearch.py <regular expression>  
#

import re, os, sys #use re for regex, os for listdir, and sys for argv  

files = os.listdir('.') #Get all files in the current directory 

for i in files: # loop through each file
	if i.endswith('.txt'):  # does the file end with .txt ? 
		txtfile = open(i) # open the file ending with .txt 
		txtfile = txtfile.read() # read the file 
		regex = re.compile(sys.argv[1]) #pass the user's argument as regex 
		find = regex.findall(txtfile) # find all occurances of the user's regex in the .txt file 
		if find: #if find equals true, meaning a match has been found. 
			print('Match in file: ' + i + '\n' + str(find))  # print the file and the match 
