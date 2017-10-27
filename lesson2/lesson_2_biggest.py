#!/usr/bin/env python

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers using knowledge from Unit2 so far
# (no MAX)

def bigger(x,y):
    if x>y:
        return x
    else:
        return y

def biggest(x,y,z):
    return bigger(bigger(x,y),z)

print biggest(5, 5, 1)
print biggest(6, 3, 9)
