import unittest

from src.repository.local_link_repository import LocalLinkRepository


URL = 'http://www.example.com'

LINKS = ['1','2','3']

class TestLocalLinkRepository(unittest.TestCase):
    def test_put_all(self):
       subject = LocalLinkRepository(None, None)
       self.assertEqual(3, subject.put_all(LINKS))

    def test_with_start_link(self):
        subject = LocalLinkRepository(None, None)
        subject.with_start_link(LINKS[0])
        self.assertEqual([LINKS[0]], subject.get_batch())

    def test_get_batch(self):
        subject = LocalLinkRepository(None, None)
        subject.put_all(LINKS)
        self.assertCountEqual(LINKS, subject.get_batch())

    def test_get_batch_doesnt_raise_key_error(self):
        subject = LocalLinkRepository(None, None)
        self.assertEqual([], subject.get_batch())

if __name__ == '__main__':
    unittest.main()
