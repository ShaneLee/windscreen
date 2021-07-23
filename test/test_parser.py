import unittest

from src.parser import Parser

from test.provider.test_file_provider import TestFileProvider

FILE = TestFileProvider().get()

subject = Parser()

class TestParser(unittest.TestCase):
    def test_find_content(self):
       self.assertEqual(8398, len(subject.find_content(FILE)))

    def test_links(self):
       self.assertEqual(16, len(subject.find_unique_article_links(FILE)))

    def test_find_metadata(self):
       url = 'https://www.ft.com/content/afc67ffb-3f4c-4b41-8240-1a96115325c9'
       headline = 'It’s not pent up demand, it’s savings'
       standfirst = 'Also, why did Jamie Dimon get a random $50m?'
       date_published = '2021-07-22T05:30:07.739Z'
       author = 'Robert Armstrong'
       category = 'Markets'
       result = subject.find_metadata(FILE)

       self.assertEqual(url, result.get_url())
       self.assertEqual(headline, result.get_headline())
       self.assertEqual(standfirst, result.get_standfirst())
       self.assertEqual(date_published, result.get_date_published())
       self.assertEqual(author, result.get_author())
       self.assertEqual(category, result.get_category())
        

if __name__ == '__main__':
    unittest.main()

