MaintenanceCheck
================

Runs the Unix maintenance scripts on OS X.

OS X runs three maintenance scripts to help clean up the system at periodic intervals: daily, weekly and monthly. However, on older versions of the OS (i.e. 10.5 Leopard and before) these scripts only run in the early hours of the morning and only if the computer is on and awake. It is quite often not the case that the computer will be in this state at this time, so the scripts do not run. This simple program checks to see if the scripts have been run recently and, if they have not, runs them.
