#!/usr/bin/env python

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

# As pointed out in 2.5 this is the complicated, this runs fast
# but it's a lot of code!

def isLeap(year):
    ''' Returns bool -- does what it says on the tin '''
    # Not a century
    if year%4==0 and year%100!=0:
        return True
    # Appropriate century
    if year%100==0 and year%400==0:
        return True
    return False

def howManyLeaps(yearstart, yearend):
    ''' Count number of leap years between and including 
    yearstart and yearend '''
    # daysBetweenDates orders args so this can be picky
    counting=yearstart
    counter=0
    while counting<=yearend:
        if isLeap(counting): 
            counter+=1 
        counting+=1
    return counter

def monthToDays(month,day):
    ''' Count days from first day of the years
    to a certain day of month '''
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    tot=0
    for i in range(0,month-1): # n2self: range goes from top-1
        tot+=months[i]
    tot+=day
    return tot

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    tot=0
    
    # If wrong order either rearranging them/printing error:
    if year1>year2 or year1==year2 and month1>month2 or \
       year1==year2 and month1==month2 and day1>day2:
        #year1, month1, day1, year2, month2, day2=\
        #    year2, month2, day2, year1, month1, day1
        return "No time travel!"
    
    if year1<1582 or year1==1582 and month1<10 or \
       year1==1582 and month1==10 and day1<15:
        print '''Your date goes back to before the start of 
        the Gregorian calendar, dates might be off.'''
    
    # Count the difference in day/month dates
    tot+=monthToDays(month2,day2)-monthToDays(month1,day1)

    # Count years & leaps:
    if abs(year2-year1)>0:
        tot+=abs(year2-year1)*365
        tot+=howManyLeaps(year1,year2)
        if month1>2 and isLeap(year1): tot-=1 # discount if past feb
        if month2<2 and isLeap(year2): tot-=1 # discount if not yet feb
    if year1==year2 and isLeap(year1):
        if month1<=2 and month2>2: tot+=1 # count if incl feb
    return tot


    
##########################################################
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

print daysBetweenDates(1400,2,2,1900,1,1)
print daysBetweenDates(2011,2,2,2010,1,1)
print daysBetweenDates(2010,5,1,2011,4,1)
