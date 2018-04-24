#!/usr/bin/env python3

import unittest
from bouncing_balls import bouncingBall

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(bouncingBall(3, 0.66, 1.5), 3)

    def test_second(self):
        self.assertEqual(bouncingBall(30, 0.66, 1.5), 15)
      
if __name__ == '__main__':
    unittest.main()

