#!/usr/bin/env python

# Write code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

myPage =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

myPage1=("potatoes")

def get_next_target(page):
    ''' Returns the first url found and the appropriate
    location to truncate the string to iterate
    and find the next one'''
    url_head='<a href="'
    url_tail='"'
    start_url=page.find(url_head)
    if start_url == -1:
        return None,0
    end_url=page.find(url_tail, start_url)
    url=page[start_url+len(url_head):end_url]
    return url, end_url

link, chop=get_next_target(myPage)
link1, chop1=get_next_target(myPage1)

print link is None, chop
print link1 is None, chop1
