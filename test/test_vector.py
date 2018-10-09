# -*- coding: utf-8 -*-

import unittest
from math import pi, sqrt

from vector_2d import *


class TestVector(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Vector(0, 0)), 'Vector(0, 0)')
        self.assertEqual(str(VectorPolar(0, 0)), 'VectorPolar(0, 0)')

    def test_abs(self):
        self.assertEqual(abs(Vector(0, 0)), 0)
        self.assertEqual(abs(Vector(5, 0)), 5)
        self.assertEqual(abs(Vector(5, 5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(0, 5)), 5)
        self.assertEqual(abs(Vector(-5, 5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(-5, 0)), 5)
        self.assertEqual(abs(Vector(-5, -5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(0, -5)), 5)
        self.assertEqual(abs(Vector(5, -5)), 5 * 2 ** 0.5)

    def test_add(self):
        self.assertEqual(Vector(5, 5) + Vector(2, 1), Vector(7, 6))
        self.assertEqual(Vector(5, 5) + Vector(-2, 1), Vector(3, 6))
        self.assertEqual(Vector(-5, -5) + Vector(-2, -1), Vector(-7, -6))

    def test_sub(self):
        self.assertEqual(Vector(5, 5) - Vector(2, 1), Vector(3, 4))
        self.assertEqual(Vector(5, 5) - Vector(-2, 1), Vector(7, 4))
        self.assertEqual(Vector(-5, -5) - Vector(-2, -1), Vector(-3, -4))

    def test_mul(self):
        self.assertEqual(Vector(3, 5) * 7, Vector(21, 35))

    def test_unit(self):
        self.assertEqual(Vector(1, 0), Vector(6, 0).unit())
        self.assertEqual(Vector(0, 1), Vector(0, 9).unit())
        self.assertEqual(round_vector(Vector(1 / 2 ** 0.5, 1 / 2 ** 0.5)),
                         round_vector(Vector(7, 7).unit()))
        self.assertEqual(round_vector(Vector(-1 / 2 ** 0.5, 1 / 2 ** 0.5)),
                         round_vector(Vector(-8, 8).unit()))

    def test_get_comps(self):
        self.assertEqual(Vector(5, 1).get_comps(), (5, 1))
        self.assertEqual(Vector(5.2, 1.5).get_comps(), (5.2, 1.5))
        self.assertEqual(Vector(5.2, 1.6).get_comps(False), (5, 1))

    def test_set_comp(self):
        vector = Vector(0, 0)
        vector.set_comp(0, 9)
        vector.set_comp(1, 7)
        self.assertEqual(vector, Vector(9, 7))

    def test_neg(self):
        self.assertEqual(-Vector(3, 2), Vector(-3, -2))

    def test_call(self):
        vector = Vector(3, 2)
        self.assertEqual(vector(), (3, 2))
        self.assertEqual(vector(0), 3)
        self.assertEqual(vector(1), 2)

    def test_conversion_to_cartesian(self):
        self.assertEqual(round_vector(VectorPolar(1, 0).to_cartesian()), Vector(1, 0))
        self.assertEqual(round_vector(VectorPolar(1, pi / 2.0).to_cartesian()), Vector(0, 1))
        self.assertEqual(round_vector(VectorPolar(1, pi).to_cartesian()), Vector(-1, 0))
        self.assertEqual(round_vector(VectorPolar(1, 3 * pi / 2.0).to_cartesian()), Vector(0, -1))
        self.assertEqual(round_vector(VectorPolar(1, 2 * pi).to_cartesian()), Vector(1, 0))

    def test_iter_cartesian(self):
        tup = (5, 4)
        vector = Vector(*tup)
        for i, attribute in enumerate(vector):
            self.assertEqual(tup[i], attribute)

    def test_iter_polar(self):
        tup = (5, pi)
        vector = VectorPolar(*tup)
        for i, attribute in enumerate(vector):
            self.assertEqual(tup[i], attribute)

    def test_conversion_to_polar(self):
        self.assertEqual(round_vector(Vector(1, 0).to_polar()), VectorPolar(1, 0))
        self.assertEqual(Vector(0, 1).to_polar(), VectorPolar(1, pi / 2.0))
        self.assertEqual(Vector(0, -1).to_polar(), VectorPolar(1, 3 * pi / 2.0))

        vector = Vector(13, 23)
        self.assertEqual(vector, round_vector(vector.to_polar().to_cartesian()))

        vector = VectorPolar(56, 1)
        self.assertEqual(vector, round_vector(vector.to_cartesian().to_polar()))

    def test_int(self):
        self.assertEqual(Vector(3, 5).int(), (3, 5))
        self.assertEqual(Vector(3.2, 5.1).int(), (3, 5))

    def test_div(self):
        self.assertEqual(Vector(5, 5) / 2, Vector(2.5, 2.5))

    def test_angle(self):
        self.assertEqual(angle(Vector(1, 0)), 0)
        self.assertEqual(angle(Vector(1, 0), Vector(1, 0)), 0)
        self.assertEqual(angle(Vector(1, 1), Vector(1, 0)), pi / 4)
        self.assertEqual(angle(Vector(0, 1), Vector(1, 0)), pi / 2)
        self.assertEqual(angle(Vector(-1, 1), Vector(1, 0)), 3 * pi / 4)
        self.assertEqual(angle(Vector(-1, 0), Vector(1, 0)), pi)
        self.assertEqual(angle(Vector(-1, -1), Vector(1, 0)), 5 * pi / 4)
        self.assertEqual(angle(Vector(0, -1), Vector(1, 0)), 3 * pi / 2)
        self.assertEqual(angle(Vector(1, -1), Vector(1, 0)), 7 * pi / 4)

        self.assertEqual(angle(Vector(-1, -1), Vector(-1, 0)), pi / 4)
        self.assertEqual(angle(Vector(-1, 0), Vector(-1, 1)), pi / 4)

    def test_pow(self):
        self.assertEqual(Vector(5, 3) * 5 * 5, Vector(5, 3) ** 5)

    def test_rmul(self):
        self.assertEqual(0.5 * Vector(2, 2), Vector(1, 1))

    def test_distance_point_line(self):
        self.assertEqual(distance_point_line(Vector(5, 1), (Vector(), Vector(100, 0))), 1)
        self.assertEqual(distance_point_line(Vector(5, 2), (Vector(), Vector(100, 0))), 2)
        self.assertEqual(distance_point_line(Vector(100, 2), (Vector(), Vector(100, 0))), 2)
        self.assertEqual(distance_point_line(Vector(110, 2), (Vector(), Vector(100, 0))), 2)

    def test_distance_point_segment(self):
        # IN
        self.assertEqual(distance_point_segment(Vector(100, 1), (Vector(), Vector(100, 0))), 1)
        self.assertEqual(distance_point_segment(Vector(5, 2), (Vector(), Vector(100, 0))), 2)
        self.assertEqual(distance_point_segment(Vector(100, 2), (Vector(), Vector(100, 0))), 2)

        # OUT
        self.assertEqual(distance_point_segment(Vector(2, 0), (Vector(), Vector(1, 0))), 1)
        self.assertEqual(distance_point_segment(Vector(-1, 0), (Vector(), Vector(1, 0))), 1)
        self.assertEqual(distance_point_segment(Vector(1, 1), (Vector(), Vector(1, 0))), 1)
        self.assertEqual(distance_point_segment(Vector(0, 1), (Vector(), Vector(1, 0))), 1)
        self.assertAlmostEqual(distance_point_segment(Vector(2, 1), (Vector(), Vector(1, 0))), sqrt(2), places=6)
        self.assertAlmostEqual(distance_point_segment(Vector(110, 2), (Vector(), Vector(100, 0))), sqrt(104), places=6)
        self.assertAlmostEqual(distance_point_segment(Vector(-10, -2), (Vector(), Vector(100, 0))), sqrt(104), places=6)

    def test_normal(self):
        self.assertEqual(Vector(-1, 0), round_vector(Vector(0, 1).normal()))
        self.assertEqual(Vector(-1, 0), round_vector(Vector(0, 9).normal()))
        self.assertEqual(round_vector(Vector(-sqrt(2)/2, sqrt(2)/2)), round_vector(Vector(9, 9).normal()))

    def test_int_vector(self):
        self.assertEqual(Vector(0.1, 0.1).int_vector(), Vector(0, 0))
        self.assertEqual(Vector(0.9, 0.9).int_vector(), Vector(0, 0))
        self.assertEqual(Vector(1.1, 1.1).int_vector(), Vector(1, 1))
        self.assertEqual(Vector(1.1, 0.1).int_vector(), Vector(1, 0))


if __name__ == '__main__':
    unittest.main()
