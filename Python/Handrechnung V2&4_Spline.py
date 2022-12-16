# Visualisierung der Standard Spline-Punkte

from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, 0])
p_E = np.array([1, 1])
v_E = np.array([2, 0])

# Spline-Funktion erstellen
spline_fun, tmp, tmp = get_spline_functions(p_A, v_A, p_E, v_E)

# Punkte Berechnen
t = np.linspace(0, 1, 51)
p = np.zeros([51, 2])
for index in range(0, 51):
    p[index] = spline_fun(t[index])

# Abbildung erstellen
plt.title('Spline')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.plot(p[:, 0], p[:, 1], '-')
plt.axis('equal')
plt.grid()
plt.tight_layout()
plt.show()