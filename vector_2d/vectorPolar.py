# -*- coding: utf-8 -*-

from __future__ import division

from math import cos, pi, sin


class VectorPolar(object):
    def __init__(self, module: float, angle: float):
        self.__module = module
        self.__angle = angle

    @property
    def module(self) -> float:
        return self.__module

    @property
    def angle(self) -> float:
        return self.__angle

    def to_cartesian(self) -> 'Vector':
        from vector_2d import Vector
        return Vector(cos(self.__angle), sin(self.__angle)) * self.__module

    def __repr__(self):
        return type(self).__name__ + '(%r, %r)' % (self.__module, self.__angle)

    def __eq__(self, other: 'VectorPolar') -> bool:
        if other.module == self.__module and other.angle == self.__angle:
            return True
        return False

    def __iter__(self):
        return (i for i in (self.__module, self.__angle))

    def __add__(self, other):
        return (self.to_cartesian() + other.to_cartesian()).to_polar()

    def normal(self) -> 'VectorPolar':
        return VectorPolar(self.__module, self.__angle + pi/2.0)

    def unit(self) -> 'VectorPolar':
        return VectorPolar(1, self.__angle)
