# Diese Funktion berechnet Punkte entlang einer Spline mit konstanten räumliche Abständen (Verfahren 3)

from Funktionen.newton_and_bisection import *
from typing import Callable, List
import numpy as np

# Erklärung der Argumente:
#
# spline_fun: Standard Spline-Funktion
# spline_v_mag_fun: Geschwindigkeitsbetrag der Spline-Funktion
# delta_s: Gewünschten Abstände zwischen den Punkten (bei konstanter Geschwindigkeit nur ein Eintrag)
# vel_const: konstante oder beliebige Geschwindigkeit
# p_0: Wenn p_0 angegeben ist, dann soll der erste Punkt den gewünschten Abstand zum Punkt p_0 sein, ansonsten ist der erste Punkt der Start der Spline

def verfahren_3(spline_fun: Callable[[float], np.ndarray], spline_v_mag_fun: Callable[[float], float], delta_s: List, vel_const: bool, max_error: float, p_0: np.ndarray = np.empty(0)) -> np.ndarray:
    
    # Variablen initialisieren
    points = np.empty([1, 2])
    u = [0.]
    
    # Erster Punkt
    if p_0.size == 0:
        points[0] = spline_fun(0)
    else:
        points[0] = p_0
    
    for i in range(0, 10000):
        
        if vel_const:
            delta_s_index = 0
        else:
            delta_s_index = i
        
        # Zielkondition: Ende des Geschwindigkeitsprofils
        if len(delta_s) <= delta_s_index:
            break
        
        # Funktionen für das Newtonverfahren aufstellen:
        f = lambda x : np.linalg.norm(spline_fun(x) - points[i, :]) - delta_s[delta_s_index]
        df = lambda x : spline_v_mag_fun(x)
        
        # Zielkondition: Ende der Spline
        if f(1) <= 0:
            break
        
        # Newtonverfahren
        max_s_error = delta_s[delta_s_index] * max_error
        u.append(newton_and_bisection(f, df, u[i], u[i], 1, max_s_error, 100))
        
        points = np.append(points, [spline_fun(u[i+1])], 0)
    
    # p_0 wieder entfernen (falls nötig)
    if p_0.size != 0:
        points = np.delete(points, 0, 0)
    
    return points