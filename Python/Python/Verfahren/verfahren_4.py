# Diese Funktion berechnet einen Punkt mit vorgegebenem Abstand entlang einer Spline (Verfahren 2)

from Funktionen.newton_and_bisection import *
from typing import Callable, List
import numpy as np
import scipy.integrate as integrate

class verfahren_4:
    
    def __init__(self, spline_v_mag_fun: Callable[[float], float], n: int) -> None:
        self.spline_v_mag_fun = spline_v_mag_fun
        self.n = n
    
    def prepare(self) -> None:
        self.pairs_u = np.linspace(0, 1, self.n)
        self.pairs_s = np.zeros(self.pairs_u.shape)
        for i in range(self.n - 1):
            delta_s, integral_error = integrate.quad(self.spline_v_mag_fun, self.pairs_u[i], self.pairs_u[i+1])
            self.pairs_s[i+1] = self.pairs_s[i] + delta_s
        self.ready = True
    
    def get_total_length(self) -> float:
        return self.pairs_s[-1]
    
    def evaluate(self, s) -> List[float]:
        u = []
        for i in range(len(s)):
            if s[i] <= self.pairs_s[-1]:
                u.append(self.evaluate_single(s[i]))
        return u
    
    def evaluate_single(self, s) -> float:
        if s < 0 or s > self.pairs_s[-1]:
            print('s outside of range')
            return -1
        id = np.searchsorted(self.pairs_s, s)
        s_low = self.pairs_s[id-1]
        s_high = self.pairs_s[id]
        inter = (s - s_low) / (s_high - s_low)
        u = self.pairs_u[id-1] + inter * (self.pairs_u[id] - self.pairs_u[id-1])
        return u
        