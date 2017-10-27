# imports
from requests import get
from bs4 import BeautifulSoup

# TODO make a git repo
# TODO enter in a movie title as an argument, not a url
    # eh, url is kinda easier (copy paste)
# TODO run in bg getting results every hour?
# TODO make sure this reflects what you see everytime you hit the page

# TODO make this available to all my webscraping repos
def soupify(webpage):
    # get a post
    # TODO some sort of error checking here
    r = get(webpage)

    # get html from response
    # TODO can check for doctype=html formatt
    html = r.text

    # make me soup!
    # TODO some sort of error protection here
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

def get_spans(soup):
    spans = soup('span', 'meter-value')
    return spans

# NOTE currently return list of all scores because i wanna make sure im always gonna get one
    # we're ignoring this for now. we're assuming we always get the right score on first return
        # we have been getting ['7%', '0%'] which is weird
def get_score(soup):
    # BUG errors out when no span available (movie not yet rated, etc)
    # find the score in the soup
    # soup('span', 'meter-value') only returns 1 span (our target) despite having more scores on screen
        # works for me!
    # TODO break this up
    spans = soup('span', 'meter-value')
    # scores = []
    # for span in spans:
    #     scores.append(span.get_text())
    score = soup.find('span', 'meter-value').span.get_text() # NOTE only finds one
    return score

# TODO get list of divs children of div w/ id scoreStats
    # might as well use the first child div to pull the average rating out too

def get_scorestats_div(soup):
    # TODO scorestats_div('span') gives me a good list
    # TODO just return all the stats with this method
        # puhlease
    div = soup.find(id='scoreStats')
    scores = []
    spans = div('span')
    # for span in spans:
    #     print(span.next_sibling)
    return soup.find(id='scoreStats')

def get_average_rating(div):
    # NOTE average rating is NOT held in a span like the rest
        # it is just a string sitting in it's encompassing div?
    # TODO is there a cleaner, more understandle way to do this?
        # stripped_strings
    target = div.contents[1].contents[2].replace(' ', '')
    target = target.replace('\n', '')
    return target
    # return average_rating

def get_num_reviews(div):
    spans = div('span')
    # for span in spans:
    #     spantext = span.get_text()
    #         if span.
    # target = div.contents[3].contents[2]
        # maybe stripped_strings
    # return target

 # TODO might as well get fresh vs rotten review numbers too
    # if i do that i can just add them together to get num_reviews instead of scraping num_reviews
def get_num_fresh(div):
    target = div.contents[3].contents[2]
    return something

def get_num_rotten(div):
    return something
