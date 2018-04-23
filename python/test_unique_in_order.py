#!/usr/bin/env python3

import unittest
from unique_in_order import unique_in_order

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])

    def test_second(self):
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_third(self):
        self.assertEqual(unique_in_order([1,2,2,3,3]), [1,2,3])

if __name__ == '__main__':
    unittest.main()

