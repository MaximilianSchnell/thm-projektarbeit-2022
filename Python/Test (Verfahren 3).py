# Visualisierung der Spline-Punkte mit Verfahren 3

from Verfahren.verfahren_3 import *
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([1, 0])
p_E = np.array([0, 1])
v_E = np.array([1, 0])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Punkte Berechnen
points = verfahren_3(spline_fun, spline_v_mag_fun, [0.02], True, 0.001)

# Abbildung erstellen
plt.title('Standard Spline-Punkte')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.plot(points[:, 0], points[:, 1], '.')
plt.axis('equal')
plt.grid()
plt.show()