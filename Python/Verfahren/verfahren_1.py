# Diese Funktion berechnet einen Punkt mit vorgegebenem Abstand entlang einer Spline (Verfahren 1)

from math import floor, log
from Funktionen.newton_and_bisection import *
from typing import Callable, List
import numpy as np
import scipy.integrate as integrate

# Erklärung der Argumente:
#
# spline_v_mag_fun: Geschwindigkeitsbetrag der Spline-Funktion
# delta_s: Gewünschten Abstände zwischen den Punkten
# max_error: zulässiger Fehler der Strecke (muss auf Integrationsfehler und Newtonverfahren-fehler aufgeteilt werden)

def verfahren_1(spline_v_mag_fun: Callable[[float], float], delta_s: List, max_error: float) -> List[float]:
    
    # Fehler aufteilen
    max_error_simpson = max_error / 2
    max_error_newton = max_error - max_error_simpson
    
    # Variablen initialisieren
    u = []
    s = 0
    
    # Länge grob abschätzen
    u_probe = np.linspace(0, 1, 2 * 10 + 1)
    v_probe = np.empty(2 * 10 + 1)
    for i in range(len(u_probe)):
        v_probe[i] = spline_v_mag_fun(u_probe[i])
    L_rough = integrate.simpson(v_probe, u_probe)
    
    # Geeignete Anzahl an Zwischenpunkten für Simpson-Verfahren ermitteln
    n_base = floor(50 * (1 + log(L_rough / max_error_simpson / 100000, 100)))
    
    # Länge genauer bestimmen
    u_probe = np.linspace(0, 1, 2 * n_base + 1)
    v_probe = np.empty(2 * n_base + 1)
    for i in range(len(u_probe)):
        v_probe[i] = spline_v_mag_fun(u_probe[i])
    L = integrate.simpson(v_probe, u_probe)
    
    for i in range(len(delta_s)):
        
        s = s + delta_s[i]
        
        # Zielkondition: Ende der Spline
        if s >= L:
            break
        
        if s == 0:
            u.append(0)
        else:
            u.append(verfahren_1_single(spline_v_mag_fun, s, max_error_newton, s / L, floor(n_base * s / L)))
    
    return u

# Erklärung der Argumente:
#
# spline_v_mag_fun: Geschwindigkeitsbetrag der Spline-Funktion
# s: Gewünschtes Bogenmaß zwischen dem Anfang der Spline und dem gesuchten Punkt
# max_error: zulässiger Fehler für das Newtonverfahren
# u0: Startpunkt für das Newtonverfahren
# n: Anzahl der Zwischenschritte beim Simpson-Verfahren

def verfahren_1_single(spline_v_mag_fun: Callable[[float], float], s: float, max_error: float, u0: float = 0.5, n: int = 21) -> float:
    
    n = max([n, 1])
    
    def f(u: float) -> float:
        u_probe = np.linspace(0, u, 2 * n + 1)
        v_probe = np.empty(2 * n + 1)
        for i in range(len(u_probe)):
            v_probe[i] = spline_v_mag_fun(u_probe[i])
        return integrate.simpson(v_probe, u_probe) - s
    
    df = lambda u : spline_v_mag_fun(u)
    
    u = newton_and_bisection(f, df, u0, -0.1, 1.1, max_error, 100)
    
    return u