#!/usr/bin/env python

# Write code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

url_head='<a href="'
url_tail='"'

start_url=page.find(url_head)+len(url_head)
end_url=page.find(url_tail, start_url)

url=page[start_url:end_url]

print url
