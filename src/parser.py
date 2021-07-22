from bs4 import BeautifulSoup as bs

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
        
