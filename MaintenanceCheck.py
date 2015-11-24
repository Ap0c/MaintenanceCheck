# ----- Imports ----- #

import os
import time


# ----- Setup ----- #

# The number of seconds in a day, a week and a month.
SECONDS_DAY = 86400
SECONDS_WEEK = 604800
SECONDS_MONTH = 2629743


# ----- Functions ----- #

def print_info():

	"""Explains to the user what is happening upon launch."""

	print ('Running maintenance, please enter your password if asked and do '
		'not close the window once you have entered it. The program will '
		'inform you when it is done.')


def print_done():

	"""Informs the user of maintenance completion."""

	print 'Maintenance finished, you may now close the window.'


def run_daily():

	"""Checks when the daily script was last run, and runs it if necessary."""

	try:

		# Checks for the timestamp on the daily script output file.
		dailytime = os.path.getmtime("/var/log/daily.out")
		sincedaily = time.time() - dailytime

		# If it's been more than a day, runs it.
		if sincedaily > SECONDS_DAY:

			print_info()
			os.system("sudo periodic daily")

	# If the file does not exist, it's possible the script has never been run.
	except OSError:

		print_info()
		os.system("sudo periodic daily")


def run_weekly():

	"""Checks when the weekly script was last run, and runs it if necessary."""

	try:

		# Checks for the timestamp on the weekly script output file.
		weeklytime = os.path.getmtime("/var/log/weekly.out")
		sinceweekly = time.time() - weeklytime

		# If it's been more than a week, runs it.
		if sinceweekly > SECONDS_WEEK:

			print_info()
			os.system("sudo periodic weekly")

	# If the file does not exist, it's possible the script has never been run.
	except OSError:

		print_info()
		os.system("sudo periodic weekly")


def run_weekly():

	"""Checks when the monthly script was last run, and runs it if necessary."""

	try:

		# Checks for the timestamp on the monthly script output file.
		monthlytime = os.path.getmtime("/var/log/monthly.out")
		sincemonthly = time.time() - monthlytime

		# If it's been more than a month, runs it.
		if sincemonthly > SECONDS_MONTH:

			print_info()
			os.system("sudo periodic monthly")

	# If the file does not exist, it's possible the script has never been run.
	except OSError:

		print_info()
		os.system("sudo periodic monthly")


# ----- Main ----- #

if __name__ == '__main__':

	run_daily()
	run_weekly()
	run_monthly()
	print_done()
