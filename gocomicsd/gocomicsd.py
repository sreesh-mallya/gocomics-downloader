import argparse
import logging
import datetime
import os

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOGGER = logging.getLogger('gocomicsd')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = r'http://www.gocomics.com/'


def parse_args(cl_args):
    parser = argparse.ArgumentParser(description='Download comic strips from GoComics.')
    parser.add_argument('--path', type=str, help='Path to save downloaded files to.')
    parser.add_argument('--from', type=str, help='Download comic strips from date DD-MM-YYYY.')
    parser.add_argument('--to', type=str, help='Download comic strips from date DD-MM-YYYY.')
    parser.add_argument('--name', type=str, help='Comic to download. Use `--list` to view available comics.')
    parser.add_argument('--list', type=str, help='View available comics.')


def create_folders(path: str, folder_name: str) -> None:
    # TODO: Create folders for saving downloads
    pass


def get_img_src(comic: str, date: str = None) -> None:
    url = BASE_URL + comic + '/' + date
    filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']

    return img_src


def main():
    # TODO: Driver function
    pass
