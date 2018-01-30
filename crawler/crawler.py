#!/usr/bin/env python

# Slowly building a web crawler following course cs101 on Udacity.
# UPDATE: the seed page is broken, so the alternate get_page routine is a mock

# UPDATED get_page
def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="C1"> <a href="B1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1"><a href="G1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
       # elif url == "G1":
       #     return '<a href="H1"> '
    except:
        return ""
    return ""

# GENERAL get_page
'''
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
'''

def get_next_target(page):
    ''' Returns the first url found and the appropriate
    location to truncate the string to iterate
    and find the next one'''
    url_head='<a href="'
    url_tail='"'
    start_url=page.find(url_head)
    if start_url == -1:
        return None,0
    end_url=page.find(url_tail, start_url+len(url_head))
    url=page[start_url+len(url_head):end_url]
    return url, end_url

def get_all_links(page):
    list=[]
    while True:
        link, chop=get_next_target(page)
        if link:
            list.append(link)
            page=page[chop:]
        else:
            break
    return list

def union(a,b):
    for x in b: 
        if x not in a:
            a.append(x)

def index_union(a,b,index,indexlist):
    for x in b: 
        if x not in a:
            a.append(x)
            indexlist.append(index)

def add_to_index(index,keyword,url):
    for x in index:
        if keyword==x[0]:
            if url not in x[1]:
                x[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    content=content.split()
    for entry in content:
        if entry not in index: add_to_index(index,entry,url)

def lookup(index,keyword):
    for x in index:
        if x[0]==keyword: 
            return x[1]
    return []       
        
def crawl_web(seed,maxdepth):
    tocrawl=[seed]
    crawled=[]
    crawlindex=[0]
    branchcrawled=[]
    index=[]
    while tocrawl:
        page=tocrawl.pop() # Depth-first search
        content=get_page(page)
        depth=crawlindex.pop()
        if page not in branchcrawled and depth <= maxdepth:
            # i.e. if we haven't come across the page going down the current tree branch
            add_page_to_index(index,page,content)
            index_union(tocrawl,get_all_links(content),depth+1,crawlindex) # Slightly tidier list
            branchcrawled.append(page)
        if depth >= maxdepth or not get_all_links(content):
            # if the current branch exceeds max depth or terminates
            union(crawled,branchcrawled)
            branchcrawled=[]
            continue
    return index

index=crawl_web("http://www.udacity.com/cs101x/index.html",1000)
#index=crawl_web("https://www.st-andrews.ac.uk/",2)

#print index
print lookup(index, 'you')

#print crawl_web("http://www.udacity.com/cs101x/index.html",1)

#print crawl_web("http://www.udacity.com/cs101x/index.html",50)

#print crawl_web("http://top.contributors/forbiddenvoid.html",2)

#print crawl_web("A1",3)

# Currently works but unconvinced and spans branches

