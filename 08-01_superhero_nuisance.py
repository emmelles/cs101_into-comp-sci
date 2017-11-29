#!/usr/bin/env python

# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

# Long, using units 1,2 only
def fix_machine(debris, product):
    i=0
    rescue=True
    while i<len(product):
        if debris.find(product[i])!=-1:
            i+=1
        else:
            rescue=False
            break
    if rescue:
        return product
    return "Give me something that's not useless next time."

# One line:
def fix_machine_real_quick(debris,product):
    return product if set(debris).intersection(set(product))==set(product) else "Give me something that's not useless next time."

### TEST CASES ###
print "Tests for long"
print "Test case 1: ", fix_machine('UdaciousUdacitey', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... ', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

print "Tests for one line"
print "Test case 1: ", fix_machine_real_quick('UdaciousUdacitey', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine_real_quick('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine_real_quick('AEIOU and sometimes y... ', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine_real_quick('wsx0-=mttrhix', 't-shirt') == 't-shirt'