import numpy as np
import math

class RealExtensions:
    def __init__(self,a,b):
        self.a = a
        self.a = b
    
class Complex (RealExtensions):
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def _magnitude(self):
        res = np.sqrt(self.real**2 + self.imag**2)
        return res
    
    def _angle(self):
        res = math.atan(self.imag/self.real)
        return res
    
    def polar_form(self):
        theta = self._angle()
        z = self._magnitude()
        res = abs(z)*np.exp(1j*theta)
        return (z,theta)
    
class Dual (RealExtensions):
    def __init__(self,real,dual):
        self.real = real
        self.dual = dual
        
    def _magnitude(self):
        res = self.real
        return res
    
    def _angle(self):
        res = self.dual/self.real
        return res
    
    def polar_form(self):
        return (self._magnitude(),self._angle())

        