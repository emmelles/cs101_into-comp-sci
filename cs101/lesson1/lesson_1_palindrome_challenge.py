#!/usr/bin/env python

# Build code that checks whether a word is a palidrome
# (return -1 if false, 0 if true) using only knowledge from
# CS101 unit 1 as asked in Problem Set 1/2

word = "madam"
#word="apple"

reverse=word[::-1]
is_palindrome=reverse.find(word)

print is_palindrome

