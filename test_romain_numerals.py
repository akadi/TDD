#This is unit test module for get_romain_num
#See http://content.codersdojo.org/code-kata-catalogue/roman-numerals/
#For lanch test:
#$python test_romain_numeral.py

import unittest
from romain_numerals import get_romain_numerals

class TestConvertRomainNumerals(unittest.TestCase):
    """ Class for test get romain numerals """
    def test_get_romain_numerals(self):
        """
        Test get romain numerals function
        """
        self.assertEqual(get_romain_numerals(1), u'I')
        self.assertEqual(get_romain_numerals(2), u'II')
        self.assertEqual(get_romain_numerals(3), u'III')
        self.assertEqual(get_romain_numerals(11), u'XI')
        self.assertEqual(get_romain_numerals(100), u'LL')



if __name__ == '__main__':
    unittest.main()
