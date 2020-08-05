import logging
import datetime
import os

import click
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOGGER = logging.getLogger('gocomicsd')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = r'http://www.gocomics.com/'

dt_now = datetime.datetime.now().strftime("%Y-%m-%d")


def create_folders(path: str, folder_name: str) -> None:
    # TODO: Create folders for saving downloads
    pass


def get_img_src(comic: str, date: str = None) -> None:
    url = BASE_URL + comic + '/' + date
    # filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']

    return img_src


@click.group()
def cli():
    """Download comic strips from gocomics.com."""
    pass


@cli.command()
@click.option('--search', default=None, help='Search for a comic by name.')
def list(search):
    """List all available comics from gocomics.com."""

    # TODO: List comics
    if search is not None:
        click.echo(search)
    click.echo('hello')


@cli.command()
@click.option('--path', default=os.getcwd(), help='Download comic strips to path.')
@click.option('--from-date', default=dt_now, help='Download comic strips from date.')
@click.option('--to-date', default=dt_now, help='Download comic strips to date.')
@click.argument('name', type=str, required=True)
def save(path, from_date, to_date, name):
    """Download comic strips by name. This automatically creates a folder by name
    and subfolders by year and month. If options for from and to date are not passed,
    this downloads today's comic."""

    # TODO: Download gif
    click.echo(name)
