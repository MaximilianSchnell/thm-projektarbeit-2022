# Visualisierung der Spline-Punkte mit und ohne Geschwindigkeitsprofil

from Verfahren.verfahren_4 import verfahren_4
from Funktionen.velocity_profile import Trapezprofil_3_Stufen
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([3, 0])
p_E = np.array([0, 1])
v_E = np.array([2, 2])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

# Verfahren 4 vorbereiten
instance = verfahren_4(spline_v_mag_fun, 200)
instance.prepare()
L = instance.get_total_length()

# Strecken für konstante Geschwindigkeit berechnen
s_const = np.arange(0, L, L / 40)

# Geschwindigkeitsprofil erstellen und Strecken berechnen
v_profile = Trapezprofil_3_Stufen(1, 2, 3, L / 2)
s_profile = []
for t in np.arange(0, 3, 0.05):
    s_profile.append(v_profile.get_distance(t))

u_const = instance.evaluate(s_const)
u_profile = instance.evaluate(s_profile)

# Punkte berechnen
points_const = np.empty([0, 2])
for u_entry in u_const:
    points_const = np.append(points_const, [spline_fun(u_entry)], 0)

points_profile = np.empty([0, 2])
for u_entry in u_profile:
    points_profile = np.append(points_profile, [spline_fun(u_entry)], 0)

# Abbildung erstellen
plt.subplots(1, 2, sharey=True)
plt.subplot(1, 2, 1)
plt.title('Konstante Geschwindigkeit')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.plot(points_const[:,0], points_const[:,1], '.')
plt.axis('equal')
plt.grid()

plt.subplot(1, 2, 2)
plt.title('3-Stufen-Trapezgeschwindigkeitsprofil')
plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.plot(points_profile[:,0], points_profile[:,1], '.')
plt.axis('equal')
plt.grid()

plt.show()