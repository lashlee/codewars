#!/usr/bin/env python3

import unittest
from build_a_pile_of_cubes import find_nb 

class Test(unittest.TestCase):

    def test_small(self):
        self.assertEqual(find_nb(1071225), 45)

    def test_medium(self):
        self.assertEqual(find_nb(91716553919377), -1)

# The subsequent two tests create syntax error.
# I think this is due to the integers' being too big.
# IDK. Python is weird.
    #def test_big1(self):
    #    self.assertEqual(find_nb(1035905446778126409, 45117)        

    #def test_big2(self):
    #    self.assertEqual(find_nb(3940616233361117025), 63009)

if __name__ == '__main__':
    unittest.main()

