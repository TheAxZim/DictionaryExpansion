#!/usr/bin/python

import sys, os

# Author: Azeem Ilyas
#
# Dictionary Expansion of an existing dictionary.
# Converts using 3-5 different methods:
#
# 1. L33T Speak Conversion
# 2. Number Expansion
# 3. Random Character Expansion
# 4. Date Format Expansion
#
# Usage: DictionaryExp.py inputDictionary.txt outputDictionary.txt
# Expands each line ~5000 times. Be Careful with Storage (use -m flag)

minMode = False
removeSpaces = False
selectiveMode = False
flagLeet = False
flagNumExp = False
flagRChar = False
flagDF = False

# Mode Check
if "-minimal" in sys.argv or "-m" in sys.argv:
	minMode = True
if "-rspaces" in sys.argv:
	removeSpaces = True
if "-leet" in sys.argv or "-numexp" in sys.argv or "-rchar" in sys.argv or "-df" in sys.argv:
	selectiveMode = True
	if "-leet" in sys.argv:
		flagLeet = True
	elif "-numexp" in sys.argv:
		flagNumExp = True
	elif "-rchar" in sys.argv:
		flagRChar = True
	else:
		flagDF = True

# Read in Dictionary
inputDic = open(sys.argv[1], 'r')
leetFile = open("L33T_Tmp.txt", 'w')
neFile = open("NExp_Tmp.txt", 'w')
rCharFile = open("rChar_Tmp.txt", 'w')
dfFile = open("dfExp_Tmp.txt", 'w')


for line in inputDic:

	newStr = ""
	line = line.rstrip()
	if removeSpaces == True:
		line = line.replace(" ", "")

	if selectiveMode == False or flagLeet == True:
		# 1. Create L33T Conversion
		# Stores result in temporary file instead of memory
		leetList = {	
		"a":"4", 
		"e":"3", 
		"g":"6",
		"i":"1",
		"o":"0", 
		"s":"5", 
		"t":"7"
		}

		for char in line:
			if char.lower() in leetList:
				newStr = newStr + leetList[char.lower()]
			else:
				newStr = newStr + char
		leetFile.write( newStr + "\n" )


	if selectiveMode == False or flagNumExp == True:
		# 2. Create Number Expansions
		# Only up to 3 numbers expansion
		# Also prints additional numbers when i < 100

		if minMode == True:
			maxRange = 9
		else:
			maxRange = 999

		for i in range(0, maxRange):
			if i < 10:
				newStr = line + "00" + str(i)
				neFile.write( newStr + "\n")
			if i < 100:
				newStr = line + "0" + str(i)
				neFile.write( newStr + "\n")
			newStr = line + str(i)
			neFile.write( newStr + "\n")


	if selectiveMode == False or flagRChar == True:
		# 3. Create R-Special-Char Expansions
		# Uses list of some special characters
		rCharList = ["!", "@", "$", "%", "^", "&", "*"]
		for i in range(0, len(rCharList)):
			newStr = line + rCharList[i]
			rCharFile.write( newStr + "\n")



	if selectiveMode == False or flagDF == True:
		# 4. Generate D.F Expansions
		# Format MMYY & YYMM & YY
		if minMode == False:
			mm = ""
			yy = ""
			for i in range (1, 12):
				if i < 10:
					mm = "0" + str(i)
				else:
					mm = str(i)
				for j in range (0, 99):
					if j < 10:
						yy = "0" + str(j)
					else:
						yy = str(j)
					dfFile.write(line + mm + yy + "\n")
					dfFile.write(line + yy + mm + "\n")
	
			for k in range (0, 99):
				if k < 10:
					yy = "0" + str(k)
				else:
					yy = str(k)
				dfFile.write(line + yy + "\n")
	



# 5. Collate & Destroy
# Gathers all the new passwords and creates a new dictionary
# Deletes all the temporary files created for hard drive storage

leetFile = open("L33T_Tmp.txt", 'r')
neFile = open("NExp_Tmp.txt", 'r')
rCharFile = open("rChar_Tmp.txt", 'r')
dfFile = open("dfExp_Tmp.txt", 'r')

masterFile = open(sys.argv[2], 'w')

for line in leetFile:
	masterFile.write( line )
for line in neFile:
	masterFile.write( line )
for line in rCharFile:
	masterFile.write( line )
for line in dfFile:
	masterFile.write( line )

os.remove("L33T_Tmp.txt")
os.remove("NExp_Tmp.txt")
os.remove("rChar_Tmp.txt")
os.remove("dfExp_Tmp.txt")

print "Dictionary Generated: " + sys.argv[2]
