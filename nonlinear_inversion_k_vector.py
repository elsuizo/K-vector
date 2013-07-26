#!/usr/bin/env python
#*************************************************************************
#Imports
#*************************************************************************

import numpy as np
import matplotlib.pyplot as plt
from time import time

#Script de prueba
#
#Entradas del algoritmo:
#   1)  y=f(x)
#   2)  [x_mi:x_max]
#   3)  n (numero de puntos a discretizar la funcion)
#
#Salida:
#   1)  N_roots (Numero de raices)
#   2)  X_e (?)
#
#
#Entradas (asi se puede separar mejor para luego hacer una funcion)
#*************************************************************************
#Preprocessing
#*************************************************************************

x_min = -10. #El punto es importante ya que si no no es float
x_max = 10.

n=1000  #numero de muestras de nuestra base de datos

y=np.zeros(n,dtype=float)
x=np.zeros_like(y)
k_index=np.arange(n) #indices

x=x_min+((x_max-x_min)*(k_index-1)/(n-1))
#funcion a la que vamos a buscar las raices
y=np.sinc(x)

#*************************************************************************
#Realizamos el k-vector para y
#*************************************************************************

#prealocamos los vectores
s = np.zeros_like(y)
I = np.zeros_like(y)
k = np.zeros(n) #K-vector
y_busqueda = np.zeros_like(y)
vec_aux = np.zeros_like(y)

#epsilon es el numero de precision de la maquina
epsilon = np.finfo(np.float).eps
delta_epsilon = (n-1)*epsilon


I = np.argsort(y)

s = y[I]

y_min = s[0] #primer elemento
y_max = s[-1] #ultimo elemento

#Generamos la recta z(x)=mx+q

m = (y_max - y_min + 2 * delta_epsilon )/(n-1)
q = y_min - m - delta_epsilon
#funcion anonima para la recta
z = lambda x: (m*x+q)
i = np.arange(n)
z_discreto = z(i)

#Generamos el k-vector

k[0]=0
k[-1]=n

#TODO vectorizar :

for aux in xrange(1,n-1):
    vec_aux=s<z_discreto[aux]
    k[aux]=np.sum(vec_aux)

#Calculamos el delta
delta = .5*max(abs(y[1:n-1]-y[0:n-2]))#Recordar que 1/2 es 0 en  Python

#*************************************************************************
#Fin preprocesamiento
#*************************************************************************

#Ahora vamos a calcular una busqueda para un y conocido(y=0)
#*************************************************************************
y_conocido=0

y_a=y_conocido-delta
y_b=y_conocido+delta


j_b=np.floor((y_a-q)/m);

j_t=np.ceil((y_b-q)/m);

k_start = k[j_b]+1
k_end = k[j_t]

k_busqueda = np.arange(int(k_start),int(k_end))


y_busqueda = s[k_busqueda]

#Ahora si la cantidad de elementos de la base de datos es grande en promedio la
#cantidad de elementos que estan fuera del rango E0 =1 entonces esta en algunos
#de los dos extremos

if y_busqueda[0]<y_a:
    y_busqueda=np.delete(y_busqueda,0)

if y_busqueda[-1]>y_b:
    y_busqueda=np.delete(y_busqueda,len(y_busqueda)-1)

X=x[I[k_busqueda]]
Y=y[I[k_busqueda]]

Roots=np.unique(np.around(X))

for i in xrange(len(Roots)):

    print 'Raiz:%d ---> %d\n' %(i,Roots[i])



