# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:55:03 2021

@author: jtintore
"""

import numpy as np


#definimos algunas variables 

#primera y segunda excentricidad
primera_excentricidad=0.08199189
segunda_excentricidad=0.08226889

#cuadrdado de la segunda excentricidad
e=(segunda_excentricidad)**2

#radio polar de curvatura
c=6399594
#aplanamiento
alpha=1/297


def decimal_to_utm(long, lat):
    
    
    if long == None or lat == None:
        X = 0.0
        Y = 0.0
        huso = 0.0
    else:
        print(1)
        long= float(long)
        lat=float(lat)
        print(long,lat)
        #pasamos longitud y latitud a radianes
        long_rad= (long*np.pi)/180 #lambda
        lat_rad= (lat*np.pi)/180 # theta
        
        #buscamos el huso y nos quedamos con el entero
        huso=int((long/6)+31)
    
        #distancia angular entre la longitud y el meridiano central del huso
        #RADIANES
        distancia_anguar_long= long_rad - (huso*6 -183)*(np.pi/180) # diferencia lambda
        
        #Calculo ecuaciones Coticchia-Surace
        
        A=np.cos(lat_rad)*np.sin(distancia_anguar_long)
        
        xi = 0.5*np.log((1+A)/(1-A))
        
        eta = np.arctan(np.tan(lat_rad)/np.cos(distancia_anguar_long)) - lat_rad
        
        v = ((c)/(1+e*(np.cos(lat_rad)**2))**0.5*0.9996)
    
        zeta = (e/2)*xi**2*(np.cos(lat_rad))**2
        
        A1 = np.sin(2*lat_rad)
        
        A2 = A1*(np.cos(lat_rad))**2
        
        j2 = (lat_rad + (A1/2))
        
        j4 = ((3*j2+A2)/4)
        
        j6 = ((5*j4+A2*(np.cos(lat_rad))**2)/3)
        
        alpha = ((3/4)*e)
        
        beta = ((5/3)*(alpha)**2)
        
        gama = ((35/27)*(alpha)**3)
        
        Bo = (0.9996*c*(lat_rad-(alpha*j2)+(beta*j4)-(gama*j6)))
        
        X = ((xi*v*(1+(zeta/3))) + 500000)
        
        Y = (eta*v*(1+zeta))+Bo
    
    return X,Y, huso
