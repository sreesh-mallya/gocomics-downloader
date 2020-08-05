from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from gocomicsd.commons import BASE_URL, HEADERS, LIST_PATH


def get_titles(search: str = None):
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
