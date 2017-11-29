#!/usr/bin/env python
alphabet=list("abcdefghijklmnopqrstuvwxyz")

def freq_analysis(message):
    freq_list=[]
    for x in alphabet:
        freq_list.append(list(message).count(x)*1.0/len(list(message)))
    return freq_list



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
