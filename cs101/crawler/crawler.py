#!/usr/bin/env python

# Write code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

myPage =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

myPage1=('''Comics I enjoy:<a href="http://threewordphrase.com/">Three Word Phrase</a>,
        <a href="http://www.smbc-comics.com/">SMBC</a>,
        <a href="http://www.qwantz.com">Dinosaur Comics</a>,
        <a href="http://oglaf.com/">Oglaf</a> (nsfw),
        <a href="http://www.asofterworld.com">A Softer World</a>,
        <a href="http://buttersafe.com/">Buttersafe</a>,
        <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>,
        <a href="http://questionablecontent.net/">Questionable Content</a>,
        <a href="http://www.buttercupfestival.com/">Buttercup Festival</a>,
        <a href="http://www.mspaintadventures.com/?s=6&p=001901">Homestuck</a>,''')

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

def print_all_links(page):
    while True:
        link, chop=get_next_target(page)
        if link:
            print link
            page=page[chop:]
        else:
            break

print_all_links(myPage1)
