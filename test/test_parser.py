import unittest
import pkgutil

from src.parser import Parser

FILE = pkgutil.get_data(__name__, "test.html")

subject = Parser()

class TestParser(unittest.TestCase):
    def test_find_content(self):
       self.assertEqual(8398, len(subject.find_content(FILE)))

    def test_links(self):
       self.assertEqual(16, len(subject.find_unique_article_links(FILE)))

if __name__ == '__main__':
    unittest.main()

