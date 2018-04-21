#!/usr/bin/env python3

import unittest
from tribonacci_sequence import tribonacci 

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])

    def test_second(self):
        self.assertEqual(tribonacci([1, 1, 1], 1), [1]) 

    def test_third(self):
        self.assertEqual(tribonacci([300, 200, 100], 0), [])

    def test_fourth(self):
        self.assertEqual(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])
      
if __name__ == '__main__':
    unittest.main()

