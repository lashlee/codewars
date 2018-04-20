#!/usr/bin/env python3

import unittest
from persistent_bugger import persistence 

class Test(unittest.TestCase):

    def test_two_digit(self):
        self.assertEqual(persistence(39), 3)

    def test_three_digit(self):
        self.assertEqual(persistence(999),4)

    def test_one_digit(self):
        self.assertEqual(persistence(4),0)

if __name__ == '__main__':
    unittest.main()

