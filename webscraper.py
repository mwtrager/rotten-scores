# imports
from requests import get
from bs4 import BeautifulSoup

# TODO make a git repo
# TODO enter in a movie title as an argument, not a url
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
def get_score(soup):
    # find the score in the soup
    # soup('span', 'meter-value') only returns 1 span (our target) despite having more scores on screen
        # works for me!
    # TODO break this up
    spans = soup('span', 'meter-value')
    scores = []
    for span in spans:
        scores.append(span.get_text())
    # score = soup.find('span', 'meter-value').span.get_text() # NOTE only finds one
    return scores
