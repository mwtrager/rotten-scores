from webscraper import *
from datetime import datetime
import time
import sys
import os

# TODO since I'm writing to files and doing all this sys and os stuff
    # I really need to start try catching and doing error checking

# get url from args
url = sys.argv[1] # [0] is the script name'

# default output_path to ./output
output_path = os.getcwd() + '/output/'

# build output folder
os.makedirs(output_path, exist_ok=True)

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

# get average rating
average_rating = get_average_rating(scorestats_div)
print('Average Rating:', average_rating)

# get number of fresh reviews
num_fresh = get_num_fresh(scorestats_div)
print('Fresh reviews:', num_fresh)

# get number of rotten reviews
num_rotten = get_num_rotten(scorestats_div)
print('Rotten reviews:', num_rotten)

# print total number of reviews
num_reviews = get_num_reviews(scorestats_div)
print('Total number of reviews:', num_reviews)

# get score from soup
score = get_score(soup)

# build string
    # TODO i should really include the date here
string = 'It\'s ' + day_str+'@'+hour+':'+minute+ampm + ' and the TOMATOMETER® reads ' + str(score)+'%' + '\n'
print(string)

print(output_path+filename)
file = open(output_path+filename, 'a') # opens a file to append or creates one if one doesn't exist
file.write(string)

file.close()

# TODO run this program every hour
    # scheduled bash script can easily kick it off every hour?
    # store the results in a file, no need for db here
