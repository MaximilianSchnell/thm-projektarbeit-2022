from math import sqrt
from Verfahren.verfahren_4 import verfahren_4
from Funktionen.spline import *
import numpy as np
import matplotlib.pyplot as plt


pairs_u = [0.  , 0.05, 0.1 , 0.15, 0.2 , 0.25, 0.3 , 0.35, 0.4 , 0.45, 0.5 ,
       0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 , 0.85, 0.9 , 0.95, 1.  ]
pairs_s = [0.        , 0.09313807, 0.17518266, 0.25010905, 0.32157007,
       0.39243225, 0.46452558, 0.53868968, 0.61499267, 0.69297872,
       0.7718787 , 0.85077867, 0.92876472, 1.00506771, 1.07923181,
       1.15132514, 1.22218732, 1.29364834, 1.36857473, 1.45061932,
       1.54375739]

# Abbildung erstellen
plt.title('Wertepaare als Funktion')
plt.xlabel('Interpolationsparameter')
plt.ylabel('Strecke')
plt.plot([0, 1], [0, pairs_s[-1]], '--', c='.5')
plt.plot(pairs_u, pairs_s, '-')
plt.grid()
plt.tight_layout()
plt.show()