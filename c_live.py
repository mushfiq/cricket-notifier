"""
    this module show notifcation based on user input url and delay time
    url should be espncrickinfo url and delay should be integer
    example use python c_live.py --url=\
    'http://www.espncricinfo.com/england-v-sri-lanka-2014/engine/\
    match/667901.html' --delay=30
"""
import time
import requests

from BeautifulSoup import BeautifulSoup
from pync import Notifier

from utils import parse_input

class CrickNotfier(object):
    """this class get page soup and show the notification. """
    def __init__(self, url, delay):
        """ set url, notification delay for the class """
        self.url = url
        self.delay = delay
        self.match_title = self.url.split('/')[3]
    def _get_soup(self):
        """ prepare page soup from from url """
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise Exception('Match Not Found')
        soup = BeautifulSoup(resp.content)
        return soup

    def _get_title(self, soup):
        """ get title from soup """
        title = soup.find('title').text
        try:
            return title.split('|')[0]
        except AttributeError:
            raise Exception('AttributeError Occured')

    def score(self):
        """ get score from time """
        soup = self._get_soup()
        title = self._get_title(soup)
        while title:
            return title

    def get_live_score(self):
        """ show live notification score """
        while True:
            if self.score():
                score = self.score()
                Notifier.notify(score, title=self.match_title)
                time.sleep(self.delay)            

if __name__=="__main__":
    USER_INPUT = parse_input()
    CNOTIFIER = CrickNotfier(USER_INPUT.url, int(USER_INPUT.delay))
    CNOTIFIER.get_live_score()
    