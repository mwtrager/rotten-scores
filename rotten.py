# main

from webscraper import *

# NOTE how they handle spaces. i'm going to be building urls?
    # i guess i dont have to, i'm only monitering one movie once a day once a week..
    # doesn't make sense to have to do all work
url = 'https://www.rottentomatoes.com/m/tyler_perrys_boo_2_a_madea_halloween'
soup = soupify(url)
print('spans: ' + str(get_spans(soup)))
scores = get_score(soup)
print('scores: ' + str(scores))

# TODO run this program every hour
    # scheduled bash script can easily kick it off every hour?
    # store the results in a file, no need for db here

# this also creates a file! yay
# f = open('file.txt', 'w') # opens a file with write access
# so name it with the title of the movie (maybe just use the route of the url tomatoes gives it)
