# -*- coding: utf-8 -*-
import unittest
from src.crawler import Crawler

class ConverterTest(unittest.TestCase):

    def test_crawl(self):
        self.crawler = Crawler()
        self.assertIsInstance(self.crawler.crawl(),list)

    if __name__ == '__main__':
        unittest.main()
