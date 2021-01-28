#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import dataread as dr
import sys


filename = sys.argv[1]
Data = dr.phantom_evdata(filename,pheaders=False)
Columns = {}
Keys = []

for i in enumerate(Data.keys()):
    print(str(i[0]+1) + ')',i[1])
    Columns.update({str(i[0]): i[1]})

Ncurves = int(input("Number of curves: "))

x_val = str(int(input("x value: ")) - 1)
print("Put number next to quantity: ")
for n in range(Ncurves):
    Keys.append(str(int(input("Curve number "+ str(n+1) + ": ")) - 1))

for k in Keys:
    plt.loglog(Data[Columns[x_val]], Data[Columns[k]])
plt.show()