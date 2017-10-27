# main

# TODO generate an email to nysupport@blkmtn.com at monday 3pm

from webscraper import *
from datetime import datetime
import time
import sys

# get url from args
url = sys.argv[1] # [0] is the script name

def get_filename(url):
    # TODO error checking here? or before?
    return url.split('/')[-1]

# make filename from url
filename = get_filename(url)

# get the title of the movie from url
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

# get scorestats
scorestats_div = get_scorestats_div(soup)
average_rating = get_average_rating(scorestats_div)
print('Average Rating:', average_rating)

# get score from soup
score = get_score(soup)
string = 'It\'s ' + day_str+'@'+hour+':'+minute+ampm + ' and the TOMATOMETER® reads ' + str(score)+'%' + '\n'
print(string)

# this also creates a file! yay
file = open('./output/'+filename, 'a') # opens a file with write access
file.write(string)

file.close()

# TODO run this program every hour
    # scheduled bash script can easily kick it off every hour?
    # store the results in a file, no need for db here
