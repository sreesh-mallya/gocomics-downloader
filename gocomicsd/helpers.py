import os
from typing import Dict
from urllib.error import ContentTooShortError
from urllib.request import Request, urlopen, urlretrieve

from bs4 import BeautifulSoup

from gocomicsd.commons import BASE_URL, HEADERS, LIST_PATH, FILENAME
from gocomicsd.exceptions import InvalidPathException


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


def create_dirs(title: str, name: str, path: str, date: str):
    if not os.path.isdir(path):
        raise InvalidPathException('`path` is not a directory or `path` does not exist.')

    date_list = date.split('-')
    year = date_list[0]
    month = date_list[1]

    create_path = os.path.join(path, name, year, month)

    if not os.path.isdir(create_path):
        try:
            os.makedirs(create_path)
        except OSError as e:
            print(e)
            # TODO: Handle exception
            return None

    return create_path


def save_title_for_date(title: str, path: str, date: str):
    source = get_img_src(title, date.replace('-', '/'))
    filename = FILENAME.format(title, date)

    try:
        file_path = os.path.join(path, filename)
        urlretrieve(source, file_path)  # Save file with `filename`
    except ContentTooShortError as e:
        print(e)
        # TODO: Handle exception
        return False

    return True


def get_img_src(title: str, date: str = None) -> str:
    url = '{}/{}/{}'.format(BASE_URL, title, date)
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']

    return img_src
