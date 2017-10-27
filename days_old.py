#!/usr/bin/env python

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def isLeap(year):
    ''' Returns bool -- does what it says on the tin '''
    # Not a century
    if year%4==0 and year%100!=0:
        return True
    # Appropriate century
    if year%100==0 and year%400==0:
        return True
    return False

def nextDay(year, month, day):
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    """Simple version: assume every month has 30 days"""
    if day==28 and month==2:
        if isLeap(year): return year, month, day+1
    if day<months[month-1]:
         return year, month, day+1
    else:
        if month<12:
            return year, month+1, 1
        else:   
            return year+1, 1, 1 

def isBefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    elif year1==year2:
        if month1 < month2:
            return True
        if month2==month1:
            return day1<day2
    return False
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # Check correct order of dates:
    assert isBefore(year1,month1,day1,year2,month2,day2), "No time travel!"

    # Gregorian error:
    if isBefore(year1,month1,day1,1582,10,15):
        print '''Your date goes back to before the start of 
        the Gregorian calendar, results might be off.'''
    
    today=(year1,month1,day1)
    counter=0
    while not isBefore(year2,month2,day2-1, *today):
        # tuples get unpacked picky in 2.7 so need the -1
        today=nextDay(*today)
        counter+=1
    return counter

# Test:

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
