# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:39:11 2018

@author: samuel
"""
import matplotlib.pyplot as plt
import numpy as np
from test import *
import os


if __name__ == '__main__':
    
    #obtenemos los archivos de los test realizados:
    path = '.'
    ficheros = []
    
    #listamos todos los ficheros:
    lstDir = os.walk(path)
    #nos quedamos sólo con los que son solución:
    for root, dirs, files in lstDir:
        for f in files:
            if '_done.xml' in f and 'sol' not in f:
                ficheros.append(f)
    
    
    #creamos tantos test como archivos tengamos:
    tests = []
    notas = []
    for i in ficheros:
        solucion = i[:len(i)-8]+'sol.xml'
        tests.append(Test())
        tests[len(tests)-1].cargar_xml(solucion)
        tests[len(tests)-1].cargar_resultado_alumno(i)
        #obtenemos las notas de cada test:
        notas.append(tests[len(tests)-1].obtener_nota())
    
    
    #Pintamos la gráfica con los examenes actuales:
      
    
    plt.axes((0.1, 0.3, 0.8, 0.6))  # Definimos la posición de los ejes
    plt.bar(np.arange(len(ficheros)), notas)  # Dibujamos el gráfico de barras
    plt.ylim(0,10)  # Limitamos los valores del eje y al range definido [450, 550]
    plt.title('Notas obtenidas en examenes:')  # Colocamos el título
    plt.xticks(np.arange(len(ficheros)), ficheros, rotation = 45)
    
    print(notas)
    
        