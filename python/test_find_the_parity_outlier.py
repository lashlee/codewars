#!/usr/bin/env python3

import unittest
from find_the_parity_outlier import find_outlier

class Test(unittest.TestCase):

    def test_first_three_even(self):
        self.assertEqual(find_outlier([4, 6, 98, 2, 3, 124]), 3)

    def test_first_three_odd(self):
        self.assertEqual(find_outlier([1, 3, 95, 101, 10, 99, 93]), 10) 

    def test_first_three_mix_1(self):
        self.assertEqual(find_outlier([1, 3, 482, 3, 83, 999961]), 482)

    def test_first_three_mix_2(self):
        self.assertEqual(find_outlier([7, 22, 98012, 32, 116]), 7)
        
if __name__ == '__main__':
    unittest.main()

