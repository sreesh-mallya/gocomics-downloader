import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOGGER = logging.getLogger('gocomicsd')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = r'http://www.gocomics.com/'
