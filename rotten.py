# main

# TODO generate an email to nysupport@blkmtn.com at monday 3pm

from webscraper import *
from datetime import datetime
import time

# give it a url or it chooses for you!
choice = input('paste a rottentomatoes url or type no\n')
if choice == 'no':
    url = 'https://www.rottentomatoes.com/m/suburbicon'
else:
    url = choice
filename = get_filename(url)

# get the title of the movie
    # TODO TODO rip this from html, what im doing here is a waste
title = filename.replace('_', ' ')
# changing to list...
title = [word.capitalize() for word in title.split()]
# back to str...
filetitle = ''
for word in title:
    filetitle = filetitle + word + ' '
print('Let\'s read the TOMATOMETER® for', filetitle)

# get the webpage and make some soup
print('requesting rottentomatoes...')
soup = soupify(url)

# timestamp is a datetime object with a lot of stuff avail to it
timestamp = datetime.fromtimestamp(time.time())

# build hours and seconds string for display and format datetime
hour = timestamp.strftime('%I') # returns current our @ 12-hour clock 0 padded
minute = timestamp.strftime('%M') # returns 0 padded minute
ampm = timestamp.strftime('%p')
day_str = timestamp.strftime('%A')

# get score from soup
score = get_score(soup)
print('It\'s', day_str+'@'+hour+':'+minute+ampm, 'and the TOMATOMETER® reads', score+'%')

# this also creates a file! yay
# file = open(filename, 'w') # opens a file with write access

# file.write('score @ ' + str(datetime.fromtimestamp(time.time()) ' is ' + str(score))

# so name it with the title of the movie (maybe just use the route of the url tomatoes gives it)

# TODO run this program every hour
    # scheduled bash script can easily kick it off every hour?
    # store the results in a file, no need for db here
