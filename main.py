#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import dataread as dr
import sys
import units as uni


Filenames = sys.argv[1:]

#Data is a list of dictionaries whose header is the key and the 
#rest of the column is the data for that header.
#Data[0] is the data of the first file in dict format.
#Data[1] of the second file and so forth.
Data = [dr.phantom_evdata(i,pheaders=False) for i in Filenames]
Keys = []
Plot_headers = []
same_keys = True


#Checks if all the files have the same headers, if not, same_keys will
#change to False.
for d in enumerate(Data):
    for k in Data:
        if k.keys() != d[1].keys():
            Columns2.append({})
            same_keys = False
    
#This will be needed when the files have different headers 
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


Ncurves = int(input("Number of curves (Default=1): ") or 1)


for n in range(Ncurves):
    Keys.append(str(int(input("y-column number "+ str(n+1) + ": ")) - 1))
    Plot_headers.append(Columns[Keys[-1]])
Phantom_headers = ['time', 'x sep. 1', 'x sep. 1', 'y sep. 1', 'sep. 1']

x_val = str(int(input("x value (Default=1): ") or 1) - 1)

#Reads headers and ask for desired units: 
#for i in Columns.values():
#    for ph_keys in Phantom_headers:
#        if i == ph_keys:
#                [Data[0][i], unit] = uni.change_unit(i,Data[0][i],ask=True)
#                if len(Data) > 1:
#                    for d in enumerate(Data[1:]):
#                        [Data[d[0]+1][i], unit] = uni.change_unit(i,d[1][i],ask=False,unit=unit)






for k in Keys:
    for d in Data:
        plt.plot(d[Columns[x_val]], d[Columns[k]])

plt.show()