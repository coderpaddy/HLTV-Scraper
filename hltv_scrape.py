from datetime import date

import requests
from bs4 import BeautifulSoup as BS

MAIN_URL = "https://www.hltv.org"
TODAY = date.today()

def get_soup(url):
    r = requests.get(url)
    soup = BS(r.content, 'html.parser')
    return soup

def check_done(bool_to_check):
    if bool_to_check:
        return "Passed"
    else:
        return "Failed"


if __name__ == "__main__":
    from _events import get_todays_events
    from _rank import get_todays_ranks
    from _results import get_todays_results
    results = get_todays_results()
    events = get_todays_events()
    rank = get_todays_ranks()
    print(f" Results: {check_done(results)} \t Events: {check_done(events)} \t Rank: {check_done(rank)}")
