# -*- coding: utf-8 -*-

from math import hypot, cos, sin


class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return type(self).__name__ + '(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def get_unit(self):
        module = float(abs(self))
        if module == 0:
            module = 99999999
        return Vector(self.x / float(module), self.y / float(module))

    def get_comps(self, f=True):
        if f:
            return self.x, self.y
        return int(self.x), int(self.y)

    def set_comp(self, comp, value):
        if comp == 0:
            self.x = value
        else:
            self.y = value

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __call__(self, comp=None):
        if comp is None:
            return self.get_comps()
        return self.get_comps()[comp]

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        return False
