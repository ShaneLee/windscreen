from bs4 import BeautifulSoup as bs

from src.models.metadata import Metadata
from src.builder.metadata_builder import MetadataBuilder

class Parser:
    def __init__(self):
        pass

    def find_content(self, html):
        soup = bs(html, 'html.parser')
        p = soup.find('article').find_all('p')
        return ''.join(
            map(lambda x: x.replace('\u2009', ' '),
            map(lambda x: x.text, p)))

    def find_unique_article_links(self, html):
        soup = bs(html, 'html.parser')
        links = soup.find_all('a')
        return set(
            filter(lambda x: 'content' in x, 
            map(lambda x: x.get('href'), links)))

    def find_metadata(self, html):
        soup = bs(html, 'html.parser')
        return MetadataBuilder(True).with_url(self._find_url(soup)) .with_headline(self._find_headline(soup)) .with_standfirst(self._find_standfirst(soup)) .with_date_published(self._find_date_published(soup)) .with_author(self._find_author(soup)) .with_category(self._find_category(soup)) .build()

    def _find_url(self, soup):
        return soup.find('link', {'rel': 'canonical'})['href']
        
    def _find_headline(self, soup):
        return soup.find('h1', {'class': 'headline'}).text.strip()

    def _find_standfirst(self, soup):
        return soup.find('h2', {'class': 'article-standfirst'}).text.strip()

    def _find_date_published(self, soup):
        return soup.find('time', {'itemprop': 'datePublished'})['datetime']

    def _find_author(self, soup):
        return soup.find('a', {'class':
        'article-author-byline__author'}).text.strip()

    def _find_category(self, soup):
        return soup.find('h2', {'class': 'primary-theme'}).text.strip()
