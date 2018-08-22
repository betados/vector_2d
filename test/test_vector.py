# -*- coding: utf-8 -*-

import unittest
from vector_2d.vector import Vector
from vector_2d.vectorPolar import VectorPolar
import math


def round_vector(vector):
    return Vector(round(vector.x, 2), round(vector.y, 2))


class TestVector(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Vector(0, 0)), 'Vector(0, 0)')

    def test_conversion_to_cartesian(self):
        self.assertEqual(Vector(0, 1), round_vector(VectorPolar(1, math.pi / 2.0).to_cartesian()))
        self.assertEqual(Vector(1, 0), round_vector(VectorPolar(1, 0).to_cartesian()))
