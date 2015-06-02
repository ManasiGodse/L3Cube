#Author: AIM
#L3Cube Assignment No: 1
#Problem Statement:  Making sense out of HTTP log file.

#The program parses the weblog.txt file and displays the output in a menu driven
#format. Parsing is done with the help of regex in python and the menu is provided 
#with 8 options. Details about IP address,Details about date-wise traffic,Details of 
#request methods used,Details of requested urls,Persistent/Non-Persistent connection
#type,Details of the response status,Details of user agents are all parsed and 
#displayed.

import re
import sys

#code to open the weblog.txt file specified as an argument.
try:
    file = open(sys.argv[1])
except IOError:
    print("Error opening file: " + sys.argv[1] + ". File does not exist.")
#pattern for parsing one complete record provided in the file.
pattern = r'([\d\.]+) - - \[(.*?)\] "(\w+) (.*?) (HTTP/1.[01])" (\d+) (\d+|-) "(.*?)" "(.*?)"'
#for each record in the log file, the above RE separates the following fields as:
#group 1 - IP address
#group 2 - Date and Time
#group 3 - Request method
#group 4 - Requested URLs
#group 5 - HTTP version
#group 6 - Response status
#group 7 - Response size
#group 8 - Referer
#group 9 - User agent

IP_occurrence={}
IP_count=[]
date_count=[]
date_occur={}
req_occur={}
req_count=[]
req_urls={}
requrl_count=[]
resp_count=[]
resp_occur={}
usr_agents={}
usr_count=[]
count=1
count1=1
count2=1
count3=1
count4=1
count5=1
count6=1
count7=1
http_count=[]
for line in file:
	match=re.search(pattern,line)
#code to extract the IP from the file and count the number of times each IP address occurred in the file.
	IP_count.append(match.group(1))
	if match.group(1) not in IP_occurrence:
		IP_occurrence[match.group(1)]=1
	else:
		IP_occurrence[match.group(1)]+=1
#code to extract the date and calculate date-wise traffic.
	match1=re.search(r'(.*?):',match.group(2))
	date_count.append(match1.group(1))
	if match1.group(1) not in date_occur:
		date_occur[match1.group(1)]=1
	else:
		date_occur[match1.group(1)]+=1
#code to extract request methods and count the number of times each being used.
	req_count.append(match.group(3))
	if match.group(3) not in req_occur:
		req_occur[match.group(3)]=1
	else:
		req_occur[match.group(3)]+=1
#code to extract request urls and calculate the number of times each being requested.
	req_URL=re.search(r'[\w\w\w\.(\w+)\.\c\o\m]*',match.group(4))
	hostname=req_URL.group()
	req_URL1=re.search(r'[www\.]?(\w+)(\.com)',hostname)
	hostname1=req_URL1.group(1)
	requrl_count.append(hostname1)
	if hostname1 not in req_urls:
		req_urls[hostname1]=1
	else:
		req_urls[hostname1]+=1
#code to extract response status and calculate the number of times each response status recieved.
	match3=match.group(6)
	resp_count.append(match.group(6))
	if int(match3)==200:
		count+=1
	elif int(match3)==206:
		count1+=1
	elif int(match3)==302:
		count2+=1
	elif int(match3)==304:
		count3+=1
	elif int(match3)==404:
		count4+=1
	elif int(match3)==500:
		count5+=1
#code to extract the HTTP version and calculate number of persistent and non-persisten connections.
	match4=match.group(5)
	http_count.append(match.group(5))
	if str(match4)=="HTTP/1.0":
		count6+=1
	elif str(match4)=="HTTP/1.1":
		count7+=1
#code to extract user agents and calculate the number of times each being used.
	match5=re.search(r'(\w+|-)(\d?)',match.group(9))	
	if str(match5.group(1)) =='-' or str(match5.group(1))== "User":
		a=1		
	else:
		usr_count.append(match5.group(1))
		if match5.group(1) not in usr_agents:
			usr_agents[match5.group(1)]=1
		else:
			usr_agents[match5.group(1)]+=1
			
while True:
	print "\nEnter the choice: "
	print "1)Details about IP address \n2)Details about date-wise traffic\n3)Details of Request methods used\n4)Details of requested urls\n5)Persistent/Non-Persistent connection type\n6)Details of the response status\n7)Details of user agents\n8)Exit\n"
	choice = int(input()) 
	if choice==1:
		print "IP addresses found:"	
		IP_count=set(IP_count)		#function used for creating a set of distinct IP addresses stored in the array.
		print IP_count
		print "Number of times each IP address occurred:"
		for key, value in IP_occurrence.iteritems():
			print key,":",value
	elif choice==2:
		print "Distinct Dates of web access from log:"
		date_count=set(date_count)
		print date_count
		print "Datewise Traffic"
		for key, value in date_occur.iteritems():
			print key,":",value
	elif choice==3:
		print "Request methods found:"
		req_count=set(req_count)
		print req_count
		print "Number of times each request method used"
		for key, value in req_occur.iteritems():
			print key,":",value
	elif choice==4:
		print "Request urls found:"
		requrl_count=set(requrl_count)
		print requrl_count
		print "Number of times each request url accessed"
		for key, value in req_urls.iteritems():
			print key,":",value
	elif choice==5:
		print "HTTP versions found:"
		http_count=set(http_count)
		print http_count
		print "Persistent connections (v1.1):",count7
		print "Non-Persistent connections (v1.0):",count6
	elif choice==6:
		print "Response statuses found:"
		resp_count=set(resp_count)
		print resp_count
		print "Number of successful requests (200):",count
		print "Number of partial successful requests (206):",count1
		print "Number of requests with FOUND status (302)",count2
		print "Number of requests with NOT MODIFIED status (304):",count3	
		print "Number of requests with NOT FOUND status (404):",count4
		print "Number of requests with INTERNAL SERVER ERROR status (500):",count5
	elif choice==7:
		print "User Agents found:"
		usr_count=set(usr_count)
		print usr_count
		print "Number of times each user agent used:"
		for key, value in usr_agents.iteritems():
			print key,":",value
	elif choice==8:
		quit(0)
	else:
		print "Invalid Choice."
