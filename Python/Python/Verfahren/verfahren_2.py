# Diese Funktion berechnet einen Punkt mit vorgegebenem Abstand entlang einer Spline (Verfahren 2)

from Funktionen.newton_and_bisection import *
from typing import Callable, List

# Erklärung der Argumente:
#
# spline_v_mag_fun: Geschwindigkeitsbetrag der Spline-Funktion
# delta_s: Gewünschten Abstände zwischen den Punkten

def verfahren_2(spline_v_mag_fun: Callable[[float], float], delta_s: List) -> List[float]:
    
    # Variablen initialisieren
    u = [0.]
    
    for i in range(len(delta_s)):
        u.append(verfahren_2_single(spline_v_mag_fun, u[i], delta_s[i], 5))
        
        # Zielkondition: Ende der Spline
        if u[i+1] > 1:
            u.pop(i+1)
            break
    
    u.pop(0)
    return u

# Erklärung der Argumente:
#
# spline_v_mag_fun: Geschwindigkeitsbetrag der Spline-Funktion
# u0: Startpunkt
# s: Gewünschtes Bogenmaß zwischen dem Startpunkt und dem gesuchten Punkt
# n: Anzahl der Zwischenschritte

def verfahren_2_single(spline_v_mag_fun: Callable[[float], float], u0: float, delta_s: float, n: int) -> float:
    
    u = u0
    h = delta_s / n
    
    for i in range(n):
        k1 = h / spline_v_mag_fun(u)
        k2 = h / spline_v_mag_fun(u + k1 / 2)
        k3 = h / spline_v_mag_fun(u + k2 / 2)
        k4 = h / spline_v_mag_fun(u + k3)
        u += (k1 + 2 * (k2 + k3) + k4) / 6
    
    return u