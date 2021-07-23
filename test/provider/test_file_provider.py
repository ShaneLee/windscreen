import pkgutil

from src.parser import Parser

FILE = pkgutil.get_data(__name__, "test.html")

class TestFileProvider:
    def __init__(self):
        pass

    def get(self):
        return FILE
