# -*- coding: utf-8 -*-

from __future__ import division

from math import atan2, hypot, pi, acos


class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return type(self).__name__ + '(%r, %r)' % (self.__x, self.__y)

    def __abs__(self):
        return hypot(self.__x, self.__y)

    def __add__(self, other):
        x = self.__x + other.x
        y = self.__y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.__x - other.x
        y = self.__y - other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.__x * scalar, self.__y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __pow__(self, power, modulo=None):
        if modulo:
            raise NotImplementedError
        return (self * power) * power

    def __div__(self, scalar):
        return Vector(self.__x / scalar, self.__y / scalar)

    def __truediv__(self, scalar):
        return Vector(self.__x / scalar, self.__y / scalar)

    def unit(self):
        """
        Returns the unit vector correspondent to the original one
        """
        module = abs(self)
        if module == 0:
            module = 99999999
        return Vector(self.__x / float(module), self.__y / float(module))

    def get_comps(self, f=True):
        # TODO hacer que si se construye con valores enteros siempre devuelva valores enteros
        # TODO hacer que si se construye con valores float siempre devuelva valores float
        """
        Returns a tuple with the vector components
        Float by default, integer when f=False
        :param f: bool
        :return: tuple with the vector components
        """
        if f:
            return self.__x, self.__y
        return int(self.__x), int(self.__y)

    def set_comp(self, comp, value):
        """
        A function se set component value via numerical index
        0 = x
        1 = y
        """
        if comp == 0:
            self.__x = value
        else:
            self.__y = value

    def __neg__(self):
        """ unary minus overridden """
        return Vector(-self.__x, -self.__y)

    def __call__(self, comp=None):
        if comp is None:
            return self.get_comps()
        return self.get_comps()[comp]

    def __eq__(self, other):
        if other.x == self.__x and other.y == self.__y:
            return True
        return False

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def int(self):
        return int(self.__x), int(self.__y)

    def int_vector(self):
        # TODO it could do a true round if a parameter is passed
        return Vector(int(self.__x), int(self.__y))

    def to_polar(self):
        """ converts the vector to polar coordinates """
        from vector_2d import VectorPolar
        angle = atan2(self.__y, self.__x)
        if angle < 0:
            angle = 2 * pi + angle
        return VectorPolar(abs(self), angle)

    def normal(self):
        # TODO que devuelva una tupla con las dos perpendiculares
        return self.to_polar().normal().to_cartesian().unit()

    # TODO hacer un classmethod que cree el vector entre dos puntos


def round_vector(vector, decimal_places=5):
    """"
        Return a vector with its components rounded.
        It allow compare vectors ignoring precision errors due to how floats numbers are stored as binaries
    """
    return vector.__class__(*(round(attribute, decimal_places) for attribute in vector))


def angle(first, second=Vector(1, 0)):
    """
        Returns the angle in radians between the two given vectors.
        If only one is give the return is the angle between this and the horizontal.
    """
    angles = [atan2(*reversed(first.get_comps())), atan2(*reversed(second.get_comps()))]
    for i in (0, 1):
        if angles[i] < 0:
            angles[i] = 2 * pi + angles[i]
    return max(angles) - min(angles)


def distance_point_line(point, line):
    """ Returns the distance between a point and a line. The line is given by a tuple of points """
    # TODO hacer que los puntos puedan ser polares
    p1, p2 = line
    return abs((p2.y - p1.y) * point.x - (p2.x - p1.x) * point.y + p2.x * p1.y - p2.y * p1.x) / abs(p1 - p2)


def distance_point_segment(point, line):
    b = abs(line[0] - line[1])
    angles = [0, 0]
    for i in (0, 1):
        a = abs(point - line[i])
        c = abs(point - line[i - 1])
        angles[i] = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    if sum([1 if a > pi / 2.0 else 0 for a in angles]):
        return min([abs(point - line[0]), abs(point - line[1])])
    else:
        return distance_point_line(point, line)
