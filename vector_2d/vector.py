# -*- coding: utf-8 -*-

from math import atan, hypot


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

    def unit(self):
        """
        Returns the unit vector correspondent to the original one
        """
        module = float(abs(self))
        if module == 0:
            module = 99999999
        return Vector(self.__x / float(module), self.__y / float(module))

    def get_comps(self, f=True):
        """
        Returns a tuble qith the vector components
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

    def to_polar(self):
        from vectorPolar import VectorPolar
        return VectorPolar(abs(self), atan(self.__y / self.__x))
