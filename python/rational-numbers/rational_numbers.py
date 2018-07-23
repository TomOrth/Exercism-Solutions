from __future__ import division
import math

class Rational(object):
    def __init__(self, numer, denom):
        gcd, b = sorted([numer, denom])
        while b != 0:
            gcd, b = b, gcd % b
        if denom < 0 < gcd:
            gcd = -gcd
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer * self.denom == 0: raise ValueError('Divisor is zero')
        return Rational(self.numer * other.denom, other.numer * self.denom) 

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        numer = math.pow(self.numer, power) if power > 0 or isinstance(power, float) else math.pow(self.denom, power)
        denom = math.pow(self.denom, power) if power > 0 or isinstance(power, float) else math.pow(self.numer, power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        return math.pow(base, self.numer/self.denom)
        
