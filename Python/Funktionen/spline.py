# Diese Funktion stellt die klassische Spline-Interpolation dar

import math
import numpy as np

# Erklärung der Argumente:
#
# p_A: Startpunkt
# v_A: Startgeschwindigkeit
# P_E: Endpunkt
# v_E: Endgeschwindigkeit
# delta_u: Intervalllänge des Interpolationsparameters (also Intervall von u ist [0, delta_u])

def get_spline_functions(p_A: np.ndarray, v_A: np.ndarray, p_E: np.ndarray, v_E: np.ndarray, delta_u: float = 1):
    
    # Parameter berechen:
    a = 2 * (p_A - p_E) / delta_u**3 + (v_A + v_E) / delta_u**2  # type: ignore
    b = 3 * (p_E - p_A) / delta_u**2 - (2 * v_A + v_E) / delta_u  # type: ignore
    c = v_A
    d = p_A
    
    k0 = np.dot(c, c)
    k1 = 4 * np.dot(b, c)
    k2 = 4 * np.dot(b, b) + 6 * np.dot(a, c)
    k3 = 12 * np.dot(a, b)
    k4 = 9 * np.dot(a, a)
    
    # Spline Funktionen erstellen:
    
    # Spline-Punkte
    def spline_fun(u: float) -> np.ndarray:
        return a * u**3 + b * u**2 + c * u + d
    
    # Spline-Geschwindigkeit
    def spline_v_fun(u: float) -> np.ndarray:
        return 3 * a * u**2 + 2 * b * u + c
    
    # Spline-Geschwindigkeitsbetrag (optimiert)
    def spline_v_mag_fun(u: float) -> float:
        return math.sqrt(k4 * u**4 + k3 * u**3 + k2 * u**2 + k1 * u + k0)
    
    return spline_fun, spline_v_fun, spline_v_mag_fun