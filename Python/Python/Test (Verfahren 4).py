# Visualisierung der Spline-Punkte mit Verfahren 4

from math import sqrt
from Verfahren.verfahren_4 import verfahren_4
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, -1])
p_E = np.array([0, 1])
v_E = np.array([2, 2])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Spline-Parameter berechnen
instance = verfahren_4(spline_v_mag_fun, 200)
instance.prepare()

s = np.arange(0, 2, 0.02)
u = instance.evaluate(s)

# Punkte berechnen
points = np.empty([0, 2])
for u_entry in u:
    points = np.append(points, [spline_fun(u_entry)], 0)

# Abbildung erstellen
plt.title('Standard Spline-Punkte')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.plot(points[:, 0], points[:, 1], '.')
plt.axis('equal')
plt.grid()
plt.show()