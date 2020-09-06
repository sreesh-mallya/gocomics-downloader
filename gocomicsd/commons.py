import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOGGER = logging.getLogger('gocomicsd')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = r'http://www.gocomics.com'
LIST_PATH = r'/comics/a-to-z'

INVALID_DATE_MESSAGE = 'Dates not in format YYYY-MM-DD!'
TITLE_NOT_FOUND_MESSAGE = 'Title `{}` not found!'
FILENAME = '{}-{}.gif'
