# Visualisierung zur Bestimmung der Zwischenschritte für das Simpsonverfahren

from Funktionen.spline import *
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, -2])
p_E = np.array([0, 1])
v_E = np.array([2, 2])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Längen ausrechen
L = []
n = range(501, 1, -2)

for i in n:
    u_probe = np.linspace(0, 1, i)
    v_probe = np.empty(i)
    for i2 in range(len(u_probe)):
        v_probe[i2] = spline_v_mag_fun(u_probe[i2])
    L.append(integrate.simpson(v_probe, u_probe))

# Fehler bestimmen (Basis = Berechnung mit größter Anzahl an Zwischenpunkten)
L_error = []
for i in range(len(L)):
    L_error.append(abs(1 - L[i] / L[0]))

# Abbildung erstellen
plt.title('Fehler beim Simpson-Verfahren')
plt.xlabel('Anzahl der Punkte')
plt.ylabel('Absoluter Fehler')
plt.plot(n, L_error, '.')
plt.grid()
plt.yscale('log')
plt.show()