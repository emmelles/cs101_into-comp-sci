#!/usr/bin/env python

# Write code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page='''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="http://blag.xkcd.com/">'''

link_head='<a href="'
link_tail='"'

start_link=page.find(link_head)+len(link_head)
end_link=page.find(link_tail, start_link)

link=page[start_link:end_link]

print link
