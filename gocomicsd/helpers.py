from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from gocomicsd.commons import BASE_URL, HEADERS


def create_folders(path: str, folder_name: str):
    # TODO: Create folders for saving downloads
    pass


def get_img_src(comic: str, date: str = None):
    url = BASE_URL + comic + '/' + date
    # filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'
    req = Request(url, None, HEADERS)

    with urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.find_all('picture', {'class': 'item-comic-image'})[0].img['src']

    return img_src
