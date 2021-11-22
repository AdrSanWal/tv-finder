from os.path import dirname, realpath, join
from pathlib import Path
from re import sub
from shutil import copyfile
import sqlite3
from unicodedata import normalize
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from requests import get as rget


file_folder = dirname(realpath(__file__))

# Local
where = 'local'
urls = ['film.html']
media_folder = join(file_folder, 'destination_media')


# Activate when web part works
# where = 'web'
# url_base = 'https://www.filmaffinity.com'
# # urls = [f'{url_base}/es/tour.php?idtour={_}' for _ in range(6, 23)] #  all
# urls = ['https://www.filmaffinity.com/es/tour.php?idtour=6'] # only 6
# path_folder = Path(file_folder).parent
# media_folder = join(path_folder, 'tvfinder/tvfinder/media/tvfinder')


class Sqlitedb():
    db = join(file_folder, 'db.sqlite3')

    def __init__(self):
        self.con = sqlite3.connect(Sqlitedb.db)
        self.cur = self.con.cursor()

    def create_table(self, name, *args, **kwargs):
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {name}({kwargs})''')

    def read_table(self, name, *args, **kwargs):
        if args:
            tables = ', '.join([table if args else '*' for table in args])
        else:
            tables = '*'
        conditions = [f'{key} {kwargs[key]}' for key in kwargs]
        conditions = ' '.join(conditions).replace('_', ' ')
        query = f'SELECT {tables} FROM {name} {conditions}'
        print(query)
        for row in self.cur.execute(query):
            print(row)


class Film():
    def __init__(self, title):
        self.title = title

    def slugify(self):
        """To storage movie names, removing invalid characters"""
        value = (normalize('NFKD', self.title)
                 .encode('ascii', 'ignore')
                 .decode('ascii'))
        value = sub(r'[^\w\s-]', '', value.lower())
        return sub(r'[-\s]+', '-', value).strip('-_')

    def copy_images(self, origin):
        image_path = f'{media_folder}/{self.slugify()}.jpg'
        if where == 'local':
            origin = origin.replace('..', file_folder)
            copyfile(origin, image_path)
        elif where == 'web':
            urlretrieve(origin, image_path)

    def get_fields(self, soup, field, *args, **kwargs):
        select_filter = []

        for tag_attr in zip(args, kwargs.items()):
            tag, (atribute, value) = tag_attr
            query = f'{tag}[{atribute}={value}]'
            select_filter.append(query)

        if field == 'o_t':
            query = f'{tag}[{atribute}={value}] > dl > dd'
            dl_dd_tag = soup.select_one(query).find(text=True)
            return [dl_dd_tag.strip()]

        list_tags = soup.select(' '.join(select_filter))

        if field == 'c':
            return [tag.img['alt'] for tag in list_tags]

        return [tag.get_text().strip() for tag in list_tags]

    def fill_fields(self, soup):
        self.org_title = self.get_fields(soup, 'o_t', 'div', id='left-column')
        self.year = self.get_fields(soup, 'y', 'dd', itemprop='datePublished')
        self.country = self.get_fields(soup, 'c', 'span', id='country-img')
        self.gender = self.get_fields(soup, 'g', 'span', itemprop='genre')
        self.director = self.get_fields(soup, 'd', 'span', itemprop='director')
        self.rating = self.get_fields(soup, 'r', 'div', itemprop='ratingValue')
        self.summary = self.get_fields(soup, 's', 'dd', itemprop='description')

    def __str__(self):
        return f'{self.title}'


def get_page_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
               'AppleWebKit/537.36 (KHTML, like Gecko)'
               'Chrome/39.0.2171.95 Safari/537.36'}
    response = rget(url, headers=headers)
    return response


def read_from(origin):
    if where == 'local':
        origin = join(file_folder, 'html', origin)
        with open(origin, "r") as file:
            text = file.read()
    elif where == 'web':
        text = get_page_source(origin).text
    return BeautifulSoup(text, "lxml")


for url in urls:
    soup = read_from(url)
    divs = soup.find_all('div', class_="mposter")

    for div in divs:
        a_tag = div.find("a")
        title = a_tag.get('title')

        film = Film(title)

        link = a_tag.get('href')
        url_image = a_tag.find('img').get('src')
        film.copy_images(url_image)

        film_soup = read_from(link)
        film.fill_fields(film_soup)

# bbdd = Sqlitedb()
# # bbdd.read_table('tv_tv', 'id', 'year', 'country', ORDER_BY='year')
# # bbdd.read_table('tv_tv', ORDER_BY='year')
