#!/usr/bin/env python

def row(ls,n):
    return ls[n]

def col(ls,n):
    col=[]
    i=0
    for i in range(len(ls)):
        col.append(ls[i][n])
    return col

def symmetric(ls):
    # Your code here
    if len(ls)==0:
        return True
    if not isinstance(ls[0], list):
        if len(ls)==1:
            return True
        return False
    if len(row(ls,0))!=len(ls):
        return False
    for i in range(len(ls)):
        if not row(ls,i)==col(ls,i): return False
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])

print symmetric([[1,2,3],
                 [2,3,1]])
