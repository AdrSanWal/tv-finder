from django import setup
from os import environ
from os.path import dirname, realpath, join
from re import sub
from shutil import copyfile
from unicodedata import normalize
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from requests import get as rget

environ.setdefault('DJANGO_SETTINGS_MODULE', 'tvfinder.settings')
setup()

from tv.models import Gender, Director, Tv


# # Local testing
where = 'local'
urls = ['film.html']

# Activate when web part works
# where = 'web'
# url_base = 'https://www.filmaffinity.com'
# urls = [f'{url_base}/es/tour.php?idtour={_}' for _ in [6, 80]]


file_folder = dirname(realpath(__file__))
filldb_folder = file_folder.rsplit('/', 1)[0]
media_folder = join(file_folder, 'tvfinder/media/tvfinder')


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
        file_name = self.slugify()
        image_path = f'{media_folder}/{file_name}.jpg'
        if where == 'local':
            origin = origin.replace('..', filldb_folder)
            copyfile(origin, image_path)
        elif where == 'web':
            urlretrieve(origin, image_path)
        self.photo = f'tvfinder/{file_name}.jpg'

    def get_fields(self, soup, field, *args, **kwargs):
        select_filter = []

        for tag_attr in zip(args, kwargs.items()):
            tag, (atribute, value) = tag_attr
            query = f'{tag}[{atribute}={value}]'
            select_filter.append(query)

        if field == 'o_t':
            query = f'{tag}[{atribute}={value}] > dl > dd'
            dl_dd_tag = soup.select_one(query).find(text=True)
            return dl_dd_tag.strip()

        list_tags = soup.select(' '.join(select_filter))

        if field == 'd':
            query = f'{tag}[{atribute}={value}] > a > span'
            span_a_span = soup.select(query)
            return [tag.string for tag in span_a_span]

        if field == 'c':
            country = [tag.img['alt'] for tag in list_tags]
            return country[0]

        return [tag.get_text().strip() for tag in list_tags]

    def fill_fields(self, soup):
        self.original_title = self.get_fields(soup, 'o_t', 'div', id='left-column')
        self.year = self.get_fields(soup, 'y', 'dd', itemprop='datePublished')[0]
        self.country = self.get_fields(soup, 'c', 'span', id='country-img')
        self.gender = self.get_fields(soup, 'g', 'span', itemprop='genre')
        self.tv_type = 's' if 'Serie de TV' in self.gender else 'f'
        self.seasons = 1  # Fix
        self.director = self.get_fields(soup, 'd', 'span', itemprop='director')
        rating = self.get_fields(soup, 'r', 'div', itemprop='ratingValue')[0]
        self.rating = float(rating.replace(',', '.'))
        summary = self.get_fields(soup, 's', 'dd', itemprop='description')[0]
        self.summary = summary.replace(' (FILMAFFINITY)', '')
        return {'gender': self.gender,
                'director': self.director,
                'tv_type': self.tv_type,
                'title': self.title,
                'original_title': self.original_title,
                'seasons': self.seasons,
                'photo': self.photo,
                'year': self.year,
                'country': self.country,
                'rating': self.rating,
                'summary': self.summary}

    def add_instance(*args, **kwargs):
        # Insert new genders
        id_genders = []
        for g_instance in kwargs['gender']:
            gender, _ = Gender.objects.get_or_create(gender=g_instance)
            id_genders.append(gender.id)

        # Insert new directors
        id_directors = []
        for d_instance in kwargs['director']:
            director, _ = Director.objects.get_or_create(name=d_instance,
                                                         birth=1980)
            id_directors.append(director.id)

        # Insert new tv
        tv_instance, _ = Tv.objects.get_or_create(tv_type=kwargs['tv_type'],
                                                  title=kwargs['title'],
                                                  original_title=kwargs['original_title'],
                                                  seasons=kwargs['seasons'],
                                                  photo=kwargs['photo'],
                                                  year=kwargs['year'],
                                                  country=kwargs['country'],
                                                  rating=kwargs['rating'],
                                                  summary=kwargs['summary'],
                                                  )

        # Add intermediate tables
        for id_gender in id_genders:
            tv_instance.gender.add(id_gender)
        for id_director in id_directors:
            tv_instance.director.add(id_director)

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
        origin = join(filldb_folder, 'fill_db/html', origin)
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
        title = a_tag.get('title').strip()

        # If film is already in db, skip
        if Tv.objects.filter(title=title):
            print(f'{title} is already in db ')
            continue

        film = Film(title)

        link = a_tag.get('href')
        url_image = a_tag.find('img').get('src')

        film.copy_images(url_image)

        film_soup = read_from(link)
        fields = film.fill_fields(film_soup)

        print(title)
        film.add_instance(**fields)
