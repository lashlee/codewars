#!/usr/bin/env python3

import unittest
from reverse_or_rotate import revrot

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(revrot("1234", 0), "")

    def test_second(self):
        self.assertEqual(revrot("", 0), "")

    def test_third(self):
        self.assertEqual(revrot("1234", 5), "")

    def test_fourth(self):
        self.assertEqual(revrot('733049910872815764', 5), "330479108928157")
      
if __name__ == '__main__':
    unittest.main()

