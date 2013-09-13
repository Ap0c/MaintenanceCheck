import subprocess
import os
import time

#Assigns the seconds in a day, week and month to variables.
secondsinday = 86400
secondsinweek = 604800
secondsinmonth = 2629743

def printrunning():
	print "Running maintenance, please enter your password and do not close the window once you have entered it. The program will inform you when it is done."

#Checks to see when the scripts were last run and, if it's been a while, runs them.
try:
	dailytime = os.path.getmtime("/var/log/daily.out") #Checks when the daily script output file was last modified.
	sincedaily = time.time() - dailytime
	if sincedaily > secondsinday: #If it was last modified more than a day ago, runs the script.
		printrunning()
		os.system("sudo periodic daily")
except OSError: #If the file does not exist, it's possible the script has never been run, this runs it.
	printrunning()
	os.system("sudo periodic daily")

try:
	weeklytime = os.path.getmtime("/var/log/weekly.out") #Checks when the weekly script output file was last modified.
	sinceweekly = time.time() - weeklytime
	if sinceweekly > secondsinweek: #If it was last modified more than a week ago, runs the script.
		printrunning()
		os.system("sudo periodic weekly")
except OSError: #If the file does not exist, it's possible the script has never been run, this runs it.
	printrunning()
	os.system("sudo periodic weekly")

try:
	monthlytime = os.path.getmtime("/var/log/monthly.out") #Checks when the monthly script output file was last modified.
	sincemonthly = time.time() - monthlytime
	if sincemonthly > secondsinmonth: #If it was last modified more than a month ago, runs the script.
		printrunning()
		os.system("sudo periodic monthly")
except OSError: #If the file does not exist, it's possible the script has never been run, this runs it.
	printrunning()
	os.system("sudo periodic monthly")

print "Maintenance finished, you may now close the window."