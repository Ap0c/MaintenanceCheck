import subprocess
import os
import time

#Assigns the seconds in a day, week and month to variables.
secondsinday = 86400
secondsinweek = 604800
secondsinmonth = 2629743

print "Running maintenance, do not close the window..."

#Assigns the time of modification of the maintenance script outputs (i.e. the time since they last ran) to variables, this is in Unix seconds.
dailytime = os.path.getmtime("/var/log/daily.out")
weeklytime = os.path.getmtime("/var/log/weekly.out")
monthlytime = os.path.getmtime("/var/log/monthly.out")

#Assigns the time since the scripts last ran to variables, making use of the current system time.
sincedaily = time.time() - dailytime
sinceweekly = time.time() - weeklytime
sincemonthly = time.time() - monthlytime

#Runs each script if the time since it last ran is longer than it should be.
if sincedaily > secondsinday:
	subprocess.call("sudo periodic daily")

if sinceweekly > secondsinweek:
	subprocess.call("sudo periodic weekly")

if sincemonthly > secondsinmonth:
	subprocess.call("sudo periodic monthly")

print "Maintenance finished, you may now close the window."