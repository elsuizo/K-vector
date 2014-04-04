#!/usr/bin/env python

#*************************************************************************
#imports
#*************************************************************************

import numpy as np
#import matplotlib.pyplot as plt
from time import time

#*************************************************************************
#constantes y setup
#*************************************************************************

t_start = time()
n = 10000  # numero de elementos de la base de datos
#prealocamos los vectores
y = np.zeros(n)
s = np.zeros_like(y)
i = np.zeros_like(y)
k = np.zeros_like(y)
y_busqueda = np.zeros_like(y)
vec_aux = np.zeros_like(y)

#epsilon es el numero de precision de la maquina
epsilon = np.finfo(np.float).eps
delta_epsilon = (n - 1) * epsilon

#*************************************************************************
#algoritmo
#*************************************************************************

#generamos un vector random como base de datos
y = np.random.random(n)

#luego lo ordenamos de forma ascendente

#primero obtenemos el vector de indices i del ordenamiento

i = np.argsort(y)

s = y[i]

y_min = s[0]  # primer elemento
y_max = s[-1]  # ultimo elemento

#generamos la recta z(x)=mx+q

m = (y_max - y_min + 2 * delta_epsilon) / (n - 1)
q = y_min - m - delta_epsilon
#funcion anonima para la recta
z = lambda x: (m * x + q)
i = np.arange(n)
z_discreto = z(i)

#generamos el k-vector

k[0] = 0
k[-1] = n

#todo vectorizar esto:

for aux in xrange(1, n - 1):
    vec_aux = s < z_discreto[aux]
    k[aux] = np.sum(vec_aux)


#rango de busqueda

y_a = .3
y_b = .7

j_b = np.floor((y_a - q) / m)
j_t = np.ceil((y_b - q) / m)

k_start = k[j_b] + 1
k_end = k[j_t]

k_busqueda = np.arange(int(k_start), int(k_end))


y_busqueda = s[k_busqueda]

#ahora si la cantidad de elementos de la base de datos es grande en promedio la
#cantidad de elementos que estan fuera del rango e0 =1 entonces esta en algunos
#de los dos extremos

if y_busqueda[0] < y_a:
    y_busqueda = np.delete(y_busqueda, 0)

if y_busqueda[-1] > y_b:
    y_busqueda = np.delete(y_busqueda, len(y_busqueda) - 1)

t_final = time()

print 'tiempo de procesamiento: %f' % (t_final - t_start)
