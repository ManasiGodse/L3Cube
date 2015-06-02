#Author: AIM
#L3Cube Assignment No: 5
#Problem Statement: Write a code that scans the directory for duplicate files and
#gives the user the option to remove those files.

#This program accepts the directory name as a command-line argument
#The directory is then scanned for duplicate files using md5 algorithm

#usage: python duplicate_file.py <path-to-directory>
 

import os
import sys
import md5

def remove_duplicate(dir):
	unique_file=[]
	for filename in os.listdir(dir):
		if os.path.isfile(filename):
			filehash=md5.md5(file(filename).read()).hexdigest()
		if filehash not in unique_file:
			unique_file.append(filehash)

		else:
			print "Duplicate file found: ",filename
			ch=raw_input("Do you want to remove this file? Press 1")
			if int(ch)==1:
				os.remove(filename)
				print "file deleted successfully"

if len(sys.argv)!=2:
	print "invlaid usage: specify directory path to scan for duplicate files"
	exit(1)
else:
	remove_duplicate(sys.argv[1])
