import datetime
import os
from typing import Dict
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from gocomicsd.commons import BASE_URL, HEADERS, LIST_PATH
from gocomicsd.exceptions import InvalidDateFormatError, InvalidPathException


def get_titles(search: str = None) -> Dict[str, str]:
    """
    Return a dictionary with titles against names.
    :param search: Filter titles containing search keyword.
    :return:
    """
    url = BASE_URL + LIST_PATH
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a', {'class': 'gc-blended-link gc-blended-link--primary col-12 col-sm-6 col-lg-4'})
    titles = {}

    for a in anchors:
        href = a.get('href').split('/')[1]
        name = a.find('h4', {'class': 'media-heading h4 mb-0'}).contents[0]
        if search is not None:
            if search.strip().lower() in name.lower():
                titles[href] = name
        else:
            titles[href] = name

    return titles


def is_valid_date(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True


def save_title(title: str, name: str, path: str, from_date: str, to_date: str):
    """

    :param title:
    :param path:
    :return:
    """
    if not is_valid_date(from_date) and not is_valid_date(to_date):
        raise InvalidDateFormatError('Dates not in format YYYY-MM-DD!')

    if not os.path.isdir(path):
        raise InvalidPathException('`path` is not a directory or `path` does not exist.')

    create_path = os.path.join(path, name)

    try:
        os.makedirs(create_path)
    except OSError:
        # TODO: Handle exception
        return


def get_img_src(comic: str, date: str = None):
    url = BASE_URL + comic + '/' + date
    # filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']

    return img_src
