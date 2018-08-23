# -*- coding: utf-8 -*-

from math import cos, sin


class VectorPolar(object):
    def __init__(self, module, angle):
        self.__module = module
        self.__angle = angle

    @property
    def module(self):
        return self.__module

    @property
    def angle(self):
        return self.__angle

    def to_cartesian(self):
        from vector import Vector
        return Vector(cos(self.__angle), sin(self.__angle)) * self.__module

    def __repr__(self):
        return type(self).__name__ + '(%r, %r)' % (self.__module, self.__angle)

    def __eq__(self, other):
        if other.module == self.__module and other.angle == self.__angle:
            return True
        return False

    def __iter__(self):
        return (i for i in (self.__module, self.__angle))

    def unit(self):
        return VectorPolar(1, self.__angle)
