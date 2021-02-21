#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import dataread as dr
import sys


Filenames = sys.argv[1:]

Data = [dr.phantom_evdata(i,pheaders=False) for i in Filenames]
Keys = []
same_keys = True



for d in enumerate(Data):
    for k in Data:
        if k.keys() != d[1].keys():
            Columns2.append({})
            same_keys = False
    
#This will need to be modified for several types of columns 
#It will need to make two Column dicts:
#Columns1 = {[1,2,3...] : Type columns 1 }
#Columns2 = {[1,2,3...] : Type columns 2 }
##################################################################
if same_keys == False:                                           #
    for d in enumerate(Data):                                    #
        for i in enumerate(d[1]):                                #
            print(str(i[0]+1) + ')',i[1])                        #
            Columns[d[0]].update({str(i[0]): i[1]})              #
##################################################################


#Makes a dict called Columns for the only type of columns in the input files 
#Columns = {[1,2,3...] : Columns files }
else:       
    Columns = {}
    for i in enumerate(Data[0]):
        print(str(i[0]+1) + ')',i[1])
        Columns.update({str(i[0]): i[1]})



Ncurves = int(input("Number of curves: "))

x_val = str(int(input("x value: ")) - 1)
print("Put number next to quantity: ")

for n in range(Ncurves):
    Keys.append(str(int(input("Curve number "+ str(n+1) + ": ")) - 1))

print(Columns)
for k in Keys:
    for d in Data:
        plt.plot(d[Columns[x_val]], d[Columns[k]])

plt.show() 