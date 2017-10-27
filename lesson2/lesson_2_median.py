#!/usr/bin/env python

# Define a procedure, median, that takes three
# numbers as inputs and returns the median of
# those three numbers using knowledge from Unit2 so far

def bigger(x,y):
    if x>y:
        return x
    return y

def biggest(x,y,z):
    return bigger(bigger(x,y),z)

def median(x,y,z):
    if x==biggest(x,y,z):
        return bigger(y,z)
    elif y==biggest(x,y,z):
        return bigger(x,z)
    else:
        return bigger(x,y)
    
print median(5, 5, 1)
print median(6, 3, 9)
print median(5, 2, 1)
