##Arthur A. Burkey III
##Python Drill: PyDrill_Datetime_27_idle
##Title: Datetime – Python 2.7 – IDLE

##Scenario: The company you work for just opened two new branches. One is in New York City,
##the other in London. They need a very simple program to find out if the branches are open or
##closed based on the current time of the Headquarters here in Portland. The hours of both
##branches are 9:00AM - 9:00PM in their own time zone.

##What is asked of you:
##Create code that will use the current time of the Portland HQ to find out the time in the NYC &
##London branches, then compare that time with the branches hours to see if they are open or
##closed.
##Print out if each of the two branches are open or closed.


##Guidelines:
##● Use Python 2.7 IDLE
##● Use Datetime Module
##● Execute program on the Shell

import time
from datetime import datetime
from datetime import timedelta

print datetime.now().strftime("%Y-%m-%d %H:%M is the current time/date.") 

currentTime = datetime.now().strftime("%Y-%m-%d %H:%M")
openTIME = 9
closeTIME = 21
a = 8
b = 3
portlandHour = int(datetime.now().strftime("%H"))
englandHour = portlandHour + a
newyorkHour = portlandHour + b

if portlandHour > 9 and portlandHour < 21:
        print 'Portland Branch is now open'
else:
        print 'Portland Branch is now closed'

if englandHour > 9 and englandHour < 21:
        print 'England Branch is now open'
else:
        print 'England Branch is now closed'

if newyorkHour > 9 and newyorkHour < 21:
        print 'New York Branch is now open'
else:
        print 'New York Branch is now closed'



        








