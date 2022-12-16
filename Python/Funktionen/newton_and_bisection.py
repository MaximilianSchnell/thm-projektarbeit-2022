# Diese Funktion ist eine Umsetzung des Newtonverfahrens kombiniert mit der Bisektion.

# Pakete importieren
from typing import Callable

# Erklärung der Argumente:
#
# f: Funktion deren Nullstelle gesucht wird
# df: Ableitung der Funktion f
# x_start: Startwert für das Newtonverfahren
# x_lower, x_upper: Intervall für die Bisektion
# max_error: Maximaler, zulässiger Fehler
# max_iterations: Maximale Anzahl an Iterationen

def newton_and_bisection(f: Callable[[float], float], df: Callable[[float], float], x_start: float, x_lower: float, x_upper: float, max_error: float, max_iterations: int) -> float:

    x = x_start

    for n in range(1, max_iterations):

        y = f(x)

        # Prüfen, ob der y-Wert im zulässigen Fehlerbereich liegt
        if abs(y) <= max_error:
            return x
        
        # Intervall aktualisieren
        if y > 0:
            x_upper = x
        else:
            x_lower = x
        
        # Neuer x-Wert nach Newtonverfahren
        dy = df(x)
        x = x - y / dy

        # Prüfen, ob Bisektion angewendet werden muss
        if x <= x_lower or x >= x_upper:
            x = (x_lower + x_upper) / 2
    
    print("newton_and_bisection():\nMaximale Iterationen überschritten!")
    return -999999
