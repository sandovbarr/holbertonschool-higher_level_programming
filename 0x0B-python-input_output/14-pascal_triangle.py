#!/usr/bin/python3
''' Pascal triangle '''
import math


def pascal_triangle(n):
    ''' defines the pascal traingle'''

    if n <= 0:
        return ([])
    # creamos una lista que contendra los dos primeras lineas
    pslist = [[1],[1,1]]

    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):
        # inicializamos la psline
        psline = [1]
        # bucle por cada uno de los valores de la anterior psline
        for j in range(0,len(pslist[i])-1):
            # añadimos a la pslist los nuevos valores
            # sumamos el valor de la pslist anterior con el siguinte
            psline.extend([ pslist[i][j] + pslist[i][j+1] ])
        # añadimos el ultimo valor a la nueva psline
        # siempre es un 1 igual que el primero
        psline += [1]
        # añadimos la psline a la pslist
        pslist.append(psline)
    #devolvemos la pslist ya creada
    return pslist
