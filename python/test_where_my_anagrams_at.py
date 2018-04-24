#!/usr/bin/env python3

import unittest
from where_my_anagrams_at import anagrams

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])

    def test_second(self):
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

if __name__ == '__main__':
    unittest.main()

