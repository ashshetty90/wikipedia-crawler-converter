# -*- coding: utf-8 -*-
import unittest
from src.converter import Converter

class ConverterTest(unittest.TestCase):


    def test_invalid_convert(self):
        self.converter = Converter()
        self.assertEquals(self.converter.convert('100dh####sb', 'Revenuedd#$@$#%#^EUR100 billion (2018)'),None)

    if __name__ == '__main__':
        unittest.main()
