import logging
import datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOGGER = logging.getLogger('gocomicsd')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = r'http://www.gocomics.com/'


def download(comic: str, date: str) -> None:
    url = BASE_URL + comic + '/' + date
    filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']
    urlretrieve(img_src, filename)  # Save file with `filename`
