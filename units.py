#!/usr/bin/python3
# -*- coding: utf-8 -*-


#This scripts contains physical units relevant for plotting Phantom .ev files.
#May extend eventually to a broader use 

import numpy as np
import matplotlib.pyplot as plt
import dataread as dr

#Phantom units
ptu = dr.constants.time         #Phantom time units (seconds)
pdu = dr.constants.dist         #Phantom distance units (solar rad in cm) 
pmu = dr.constants.mass         #Phantom mass units (solar mass in g)
pvu = dr.constants.vel          #Phantom velocity units (cm/s)   
peu = dr.constants.ener         #Phantom energy units (erg)
pemu = dr.constants.spener      #Phantom spec energy per mass units 
G = 1.                          #Phantom grav constant

#Other Phantom units
#Time
yrs = dr.constants.yr        #Phantom time unit in yrs
days = dr.constants.day
hours = dr.constants.hr

#Length
mts = pdu/100
au = dr.constants.au

#Mass
gr = dr.constants.mass
kg = gr/1000


