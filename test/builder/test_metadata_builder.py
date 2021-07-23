import unittest

from src.builder.metadata_builder import MetadataBuilder
from src.exception.missing_args_exception import MissingArgsException
from src.models.metadata import Metadata

URL = 'url'
HEADLINE = 'headline'
STANDFIRST = 'standfirst'
DATE_PUBLISHED = '2021_07_22'
AUTHOR = 'Gordon Bennett'
CATEGORY = 'Finance'

class TestMetadataBuilder(unittest.TestCase):
    def test_build_all_args(self):
       result = MetadataBuilder(True).with_url(URL) .with_headline(HEADLINE) .with_standfirst(STANDFIRST) .with_date_published(DATE_PUBLISHED) .with_author(AUTHOR) .with_category(CATEGORY) .build()

       expected = Metadata(
           URL, 
           HEADLINE, 
           STANDFIRST, 
           DATE_PUBLISHED,
           AUTHOR,
           CATEGORY)

       self.assertEqual(expected.get_url(), result.get_url())
       self.assertEqual(expected.get_headline(), result.get_headline())
       self.assertEqual(expected.get_standfirst(), result.get_standfirst())
       self.assertEqual(expected.get_date_published(), result.get_date_published())
       self.assertEqual(expected.get_author(), result.get_author())
       self.assertEqual(expected.get_category(), result.get_category())

    def test_build_no_args_when_all_required(self):
        try:
            MetadataBuilder(True).build()
        except MissingArgsException:
            pass
        except Exception:
            self.fail('unexpected exception raised')
        else:
            self.fail('MissingArgsException not raised')

    def test_build_some_args_when_some_required(self):
       expected = Metadata(
           URL, 
           None, 
           None, 
           None,
           None,
           None)
       result = MetadataBuilder(False).with_url(URL).build()

       self.assertEqual(expected.get_url(), result.get_url())
       self.assertEqual(expected.get_headline(), result.get_headline())
       self.assertEqual(expected.get_standfirst(), result.get_standfirst())
       self.assertEqual(expected.get_date_published(), result.get_date_published())
       self.assertEqual(expected.get_author(), result.get_author())
       self.assertEqual(expected.get_category(), result.get_category())

if __name__ == '__main__':
    unittest.main()
