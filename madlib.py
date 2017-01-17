# !/usr/bin/python3 
# Madlib exersize from chapter 8 of automate the boring stuff with python 
# See usage() function for more information. 

import sys, re #We'll use sys for cli arguments and re for the regex 


def usage():  #simple function to print script description and usage 
	print(sys.argv[0] + ' - A madlib script to read a file and replace any instance of:\n NOUN, VERB or ADJECTIVE with user input.\n\n Syntax:') 
	print(sys.argv[0] + ' <File To Read> <File To Save>') 

if len(sys.argv) < 3: #check if the user provided all the needed cli arguments if not print usage and exit. 
	print("You need to provide a file to read and a file to write the result to \n")
	usage()  
	sys.exit() 

madfile = open(sys.argv[1]) #open the file the user provided

madfile = madfile.read()  #read the file the user provided and store result as madfile 

regex = re.compile(r'NOUN|VERB|ADJECTIVE') #regex to find NOUN, VERB, or ADJECTIVE 
find = regex.findall(madfile) #find all instances of the regex and store the results in find 

for match in find: #loop through each regex match that was found.
	print('Please enter a ' + match) #Ask the user to input the match(NOUN, VERB, ADJECTIVE) 
	response = input() # Store user input as response 
	subregex = re.compile(match) #regex to find the match (NOUN, VERB, ADJECTIVE)
	madfile = subregex.sub(response,madfile, 1) #Sub the user's response for the regex match but only limit it to one match.  

print(madfile) #print the results 

madfile_result = open(sys.argv[2],'w') #open or create a user supplied filename for write. 
madfile_result.write(madfile) # the the results to the file. 
   
