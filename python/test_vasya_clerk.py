#!/usr/bin/env python3

import unittest
from vasya_clerk import tickets

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")

    def test_second(self):
        self.assertEqual(tickets([25, 100]), "NO")

if __name__ == '__main__':
    unittest.main()

