# -*- coding: utf-8 -*-

import unittest
from math import pi, sqrt

from vector_2d import *


class TestPolarVector(unittest.TestCase):
    def test_add(self):
        self.assertEqual(VectorPolar(1, 0), VectorPolar(0.5, 0) + VectorPolar(0.5, 0))
        self.assertEqual(VectorPolar(1, 0), round_vector(VectorPolar(6, 0) + VectorPolar(5, pi)))
        self.assertEqual(round_vector(VectorPolar(sqrt(2), pi / 4)),
                         round_vector(VectorPolar(1, 0) + VectorPolar(1, pi / 2)))

    def test_normal(self):
        self.assertEqual(round_vector(VectorPolar(1, pi / 2)), round_vector(VectorPolar(1, 0).normal()))
        self.assertEqual(round_vector(VectorPolar(1, pi)), round_vector(VectorPolar(1, pi / 2).normal()))


if __name__ == '__main__':
    unittest.main()
