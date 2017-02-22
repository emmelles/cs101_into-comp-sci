#!/usr/bin/env python

# Slowly building a web crawler following course cs101 on Udacity.

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

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

seed='http://www.udacity.com/cs101x/index.html'
print get_all_links(get_page(seed))
