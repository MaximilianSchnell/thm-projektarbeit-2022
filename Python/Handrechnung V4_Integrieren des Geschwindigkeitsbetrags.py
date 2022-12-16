# Visualisierung der Spline-Punkte mit Verfahren 4

from math import sqrt
from Verfahren.verfahren_4 import verfahren_4
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, 0])
p_E = np.array([1, 1])
v_E = np.array([2, 0])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Spline-Parameter berechnen
instance = verfahren_4(spline_v_mag_fun, 21)
instance.prepare()

# Spline Punkte berechnen
points_bogenmass = np.empty([0, 2])
for u_entry in range(400):
    points_bogenmass = np.append(points_bogenmass, [spline_fun(u_entry * 0.05 / 400)], 0)

points_rest = np.empty([0, 2])
for u_entry in range(200):
    points_rest = np.append(points_rest, [spline_fun(0.05 + u_entry * 0.02 / 200)], 0)

# Splinegeschwindigkeitsbetrag
points_vel = np.empty([0, 2])
for u_entry in range(200):
    points_vel = np.append(points_vel, [[u_entry * 0.07 / 200, spline_v_mag_fun(u_entry * 0.07 / 200)]], 0)

ix = np.linspace(0, 0.05, 400)
points_integral = np.zeros([1, 2])
for x_entry in ix:
    points_integral = np.append(points_integral, [[x_entry, spline_v_mag_fun(x_entry)]], 0)
verts = np.append(points_integral, [[0.05, 0]], 0)
poly = Polygon(verts, color=(1., 0., 0., 0.5))

# Abbildung erstellen
plt.subplots(2, 1)
plt.subplot(2, 1, 1)
plt.title('Geschwindigkeitsintegral')
plt.plot(points_bogenmass[:, 0], points_bogenmass[:, 1], 'r-')
plt.plot(points_rest[:, 0], points_rest[:, 1], 'b-')
plt.plot(points_bogenmass[0, 0], points_bogenmass[0, 1], 'r.')
plt.text(points_bogenmass[0, 0], points_bogenmass[0, 1], 'u0', horizontalalignment='right')
plt.plot(points_bogenmass[-1, 0], points_bogenmass[-1, 1], 'r.')
plt.text(points_bogenmass[-1, 0], points_bogenmass[-1, 1], 'u1', horizontalalignment='right')
plt.axis('equal')
plt.grid()

ax = plt.subplot(2, 1, 2)
plt.xlabel('Interpolationsparameter')
plt.ylabel('Geschwindigkeitsbetrag')
plt.plot(points_vel[:, 0], points_vel[:, 1], 'b-')
ax.add_patch(poly)
plt.grid()
plt.tight_layout()
plt.show()