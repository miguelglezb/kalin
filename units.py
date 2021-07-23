#!/usr/bin/python3
# -*- coding: utf-8 -*-


#This scripts contains physical units relevant for plotting Phantom .ev files.
#May extend eventually to a broader use 

import numpy as np
import matplotlib.pyplot as plt


#Phantom units
ptu = 1594.                     #Phantom time units (seconds)
pdu = 6.960E+10                 #Phantom distance units (solar rad in cm) 
pmu = 1.989E+33                 #Phantom mass units (solar mass in g)
pvu = 4.367E+07                 #Phantom velocity units (cm/s)   
peu = 3.793E+48                 #Phantom energy units (erg)
pemu = 1.907E+15                #Phantom spec energy per mass units 
G = 1.                          #Phantom grav constant

#Other Phantom units
#Time
yrs = ptu/(3600*24*365)         #Phantom time unit in yrs
days = ptu/(3600*24)
hours = ptu/(3600)



time_units = {'0': [1, 'Phantom time units'], '1': [yrs, 'yrs'],
              '2': [days, 'days'], '3': [hours, 'hrs']}
length_units = {'0': [1, 'Phantom length units'], '1': [pdu, 'cm']}


unit_name = {'time': time_units, 'x sep. 1': length_units, 'y sep. 1': length_units,
             'z sep. 1': length_units, 'sep. 1': length_units}


def change_unit(key,phys_quant,ask=False,unit=1):
    """change_unit(key, phys_quant, ask=False, unit=1)
        key: Name of column
        phys_quant: Values of key
        ask=False: If True, asks for a change of units for key
        unit=1"""

    if ask == True:
        print('\n**************************************')
        print('**************************************\n')
        print("You have one column named",key,'\n')
        print("Do you want to use one of the following units (applies just for Phantom data): \n")

        for i in unit_name[key]:
            if i=='0':
                print(i+') ',unit_name[key][str(i)][1],'(Default)') 
            else:
                print(i+') ',unit_name[key][str(i)][1])
        try:
            unit = unit_name[key][input()][0]
        except KeyError:
            unit = unit_name[key]['0'][0]
      
    
    changed_quant = []
    for ph in phys_quant:
        changed_quant.append(unit*ph)
    return [np.array(changed_quant), unit]