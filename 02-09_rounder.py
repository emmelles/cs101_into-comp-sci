#!/usr/bin/env python

# Build code that rounds decimal numbers correctly
# with just content from CS101 unit 1 (str, find, string ops)

#x = 3.14159
x=4.273

x=str(x+0.5)
decimal=x.find(".")

print x[0:decimal]
