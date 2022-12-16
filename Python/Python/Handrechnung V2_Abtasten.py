# Begleitende Visualisierung für die Handrechnung

from math import sqrt
from Verfahren.verfahren_2 import verfahren_2
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt

# Randbedingungen der Spline
p_A = np.array([0, 0])
v_A = np.array([2, 0])
p_E = np.array([1, 1])
v_E = np.array([2, 0])

# Spline-Funktion erstellen
spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)

u = 0.05396611525723342
k1 = 0.05810049989953899
k2 = 0.062134029378556194
k3 = 0.06239561694246138
k4 = 0.06603163265138715

# Punkte berechnen
points = np.empty([0, 2])
for i in range(400):
    u_entry = 0.05 + 0.075 * i / 400
    points = np.append(points, [[u_entry, spline_v_mag_fun(u_entry)]], 0)

# Abbildung erstellen
fig = plt.figure(figsize=(6, 2))
ax = fig.subplots()
plt.title('Abtasten')
plt.xlabel('Interpolationsparameter')
plt.ylabel('Geschwindigkeitsbetrag')
plt.plot(points[:, 0], points[:, 1], '-')
plt.plot(u, spline_v_mag_fun(u), 'r.')
plt.text(u, spline_v_mag_fun(u), 'für k1')
plt.plot(u+k1, spline_v_mag_fun(u+k1), 'r.')
plt.text(u+k1, spline_v_mag_fun(u+k1), 'für k2')
plt.plot(u+k2/2, spline_v_mag_fun(u+k2/2), 'r.')
plt.text(u+k2/2, spline_v_mag_fun(u+k2/2), 'für k3 / k4')
plt.plot(u+k3/2, spline_v_mag_fun(u+k3/2), 'r.')
# plt.axis('equal')

ax.grid()
fig.tight_layout()
plt.show()