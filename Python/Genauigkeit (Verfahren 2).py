# Visualisierung zur Bestimmung der Zwischenschritte für das Runge-Kutta-Verfahren (aus Verfahren 2)

from Verfahren.verfahren_2 import verfahren_2_single
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, -2])
p_E = np.array([0, 1])
v_E = np.array([2, 2])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Interpolationsvariablen ausrechen
u = []
n = range(501, 1, -1)

for i in n:
    u.append(verfahren_2_single(spline_v_mag_fun, 0, 0.1, i))

# Fehler bestimmen (Basis = Berechnung mit größter Anzahl an Zwischenpunkten)
u_error = []
for i in range(len(u)):
    u_error.append(abs(1 - u[i] / u[0]))

# Abbildung erstellen
plt.title('Fehler beim Runge-Kutta-Verfahren')
plt.xlabel('Anzahl der Punkte')
plt.ylabel('Absoluter Fehler')
plt.plot(n, u_error, '.')
plt.grid()
plt.yscale('log')
plt.show()