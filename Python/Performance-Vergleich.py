# In diesem Program werden die Verfahren anhand ihrer Performance verglichen

from typing import List
from Verfahren.verfahren_1 import verfahren_1
from Verfahren.verfahren_2 import verfahren_2
from Verfahren.verfahren_3 import verfahren_3
from Verfahren.verfahren_4 import verfahren_4
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt
import timeit
from random import random

n = 200

v1 = []
v2 = []
v3 = []
v4_pre = []
v4_total = []

for i in range(n):
    # Randbedingungen der Spline
    p_A = np.array([0, 0])
    v_A = np.array([2*random()-1, 2*random()-1])
    p_E = np.array([2*random()+1, 2*random()+1])
    v_E = np.array([2*random()-1, 2*random()-1])

    # Spline-Funktion erstellen
    spline_fun, tmp, spline_v_mag_fun = get_spline_functions(p_A, v_A, p_E, v_E)
    
    # Verfahren 1
    start_time = timeit.default_timer()
    
    delta_s = [0] + [0.02] * 500
    u = verfahren_1(spline_v_mag_fun, delta_s, 0.0002)

    points = np.empty([0, 2])
    for u_entry in u:
        points = np.append(points, [spline_fun(u_entry)], 0)
    
    v1.append(timeit.default_timer() - start_time)
    
    # Verfahren 2
    start_time = timeit.default_timer()
    
    delta_s = [0] + [0.02] * 500
    u = verfahren_2(spline_v_mag_fun, delta_s)

    points = np.empty([0, 2])
    for u_entry in u:
        points = np.append(points, [spline_fun(u_entry)], 0)
    
    v2.append(timeit.default_timer() - start_time)
    
    # Verfahren 3
    start_time = timeit.default_timer()
    
    points = verfahren_3(spline_fun, spline_v_mag_fun, [0.02], True, 0.001)
    
    v3.append(timeit.default_timer() - start_time)
    
    # Verfahren 4
    start_time = timeit.default_timer()
    
    instance = verfahren_4(spline_v_mag_fun, 100)
    instance.prepare()
    
    v4_pre.append(timeit.default_timer() - start_time)
    
    s = np.arange(0, 10, 0.02)
    u = instance.evaluate(s)

    points = np.empty([0, 2])
    for u_entry in u:
        points = np.append(points, [spline_fun(u_entry)], 0)
    
    v4_total.append(timeit.default_timer() - start_time)

# Ergebnisse ausgeben
print('Test mit ' + str(n) + ' Iterationen')
print('Ergebnisse:')

def mean(list: List[float]) -> float:
    return sum(list) / len(list)

print('Verfahren 1: ' + str(mean(v1)))
print('Verfahren 2: ' + str(mean(v2)))
print('Verfahren 3: ' + str(mean(v3)))
print('Verfahren 4: ' + str(mean(v4_total)))

print('Verfahren 4 (pre): ' + str(mean(v4_pre)))