#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import dataread as dr
import sys


Filenames = sys.argv[1:]

Data = [dr.phantom_evdata(i,pheaders=False) for i in Filenames]
Columns = []
Keys = []

#This will change when we mix two diffent TYPE of sets of columns 

for d in enumerate(Data):
    Columns.append({})


for i in enumerate(d[1]):
        print(str(i[0]+1) + ')',i[1])
        Columns[d[0]].update({str(i[0]): i[1]})

#Columns is [{[1,2,3...]:Columns file 1}, {[1,2,3...]:Columns file 2}...]

Ncurves = int(input("Number of curves: "))

x_val = str(int(input("x value: ")) - 1)
print("Put number next to quantity: ")

for n in range(Ncurves):
    Keys.append(str(int(input("Curve number "+ str(n+1) + ": ")) - 1))

for k in Keys:
    for d in Data:
        for c in Columns:
            plt.plot(d[c[x_val]], d[c[k]])

plt.show() 