# ----- Imports ----- #

import os
import time


# ----- Setup ----- #

# The number of seconds in a day, a week and a month.
SECONDS_DAY = 86400
SECONDS_WEEK = 604800
SECONDS_MONTH = 2629743


# ----- Functions ----- #

def print_launch():

	"""Explains to the user what is happening upon launch."""

	print ('Running maintenance, please enter your password if asked and do '
		'not close the window once you have entered it. The program will '
		'inform you when it is done.\n')


def print_info(script):

	"""Informs the user of a maintenance script running."""

	print '%s maintenance script running...\n' % script


def print_done():

	"""Informs the user of maintenance completion."""

	print 'Maintenance finished, you may now close the window.'


def run_script(script):

	"""Runs a specified script, and informs the user."""

	print_info()
	os.system('sudo periodic %s' % script)


def maintenance(script, time_period):

	"""Checks when a script was last run, and runs it if necessary."""

	try:

		# Checks for the timestamp on the daily script output file.
		last_run = os.path.getmtime('/var/log/%s.out' % script)

	# If the file does not exist, it's possible the script has never been run.
	except OSError:

		run_script(script)

	else:

		since_run = time.time() - last_run

		# If it's been more than the recommended time period, runs it.
		if sincedaily > time_period:
			run_script(script)


# ----- Main ----- #

if __name__ == '__main__':

	print_launch()

	maintenance('daily', SECONDS_DAY)
	maintenance('weekly', SECONDS_WEEK)
	maintenance('monthly', SECONDS_MONTH)

	print_done()
