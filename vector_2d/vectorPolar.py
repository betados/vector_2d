# -*- coding: utf-8 -*-

from math import hypot, cos, sin
from vector import Vector


class VectorPolar(object):
    # TODO inherit form Vector
    def __init__(self, module, argument):
        self.module = module
        self.argument = argument

    def to_cartesian(self):
        return Vector(cos(self.argument), sin(self.argument)) * self.module

    def __repr__(self):
        return 'VectorPolar(%r, %r)' % (self.module, self.argument)
