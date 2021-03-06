# imports
from requests import get
from bs4 import BeautifulSoup

# TODO make this available to all my webscraping repos
def soupify(webpage):
    # get a post
    # TODO some sort of error checking here
    r = get(webpage)

    # get html from response
    # TODO can check for doctype=html format
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
    score = soup.find('span', 'meter-value').span.get_text() # NOTE only finds one
    return score

def get_scorestats_div(soup):
    return soup.find(id='scoreStats')

def get_average_rating(div):
    # NOTE average rating is NOT held in a span like the rest
        # it is just a string sitting in it's encompassing div?
    # TODO is there a cleaner, more understandle way to do this?
        # stripped_strings
    target = div.contents[1].contents[2].replace(' ', '')
    target = target.replace('\n', '')
    return target

def get_num_reviews(div):
    # NOTE exclude the first span because it is average rating
    spans = div('span')[1:]

    # get total review number
    idx=0
    while (idx < len(spans)):
        if spans[idx].get_text().lower() == 'reviews counted: ':
            return int(spans[idx+1].get_text())
        idx = idx + 1

def get_num_rotten(div):
    # NOTE exclude the first span because it is average rating
    spans = div('span')[1:] # TODO error check needed, array out of bounds exception if list empty

    # get rotten review number
    idx=0
    while (idx < len(spans)):
        if spans[idx].get_text().lower() == 'rotten: ':
            return int(spans[idx+1].get_text())
        idx = idx + 1

def get_num_fresh(div):
    # NOTE exclude the first span because it is average rating
    spans = div('span')[1:] # TODO error check needed, array out of bounds exception if list empty

    # get fresh review number
    idx=0
    while (idx < len(spans)):
        if spans[idx].get_text().lower() == 'fresh: ':
            return int(spans[idx+1].get_text())
        idx = idx + 1

def is_scored(soup):
    # TODO check if there is a score yet
    target = soup('p', 'noReviewText')
    return not len(target) > 0

def get_movie_title(soup):
    title = soup.find(id='movie-title').get_text().strip()
    return title
