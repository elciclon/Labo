#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:59:17 2026

@author: adrian
"""
import csv

def materias_cuatrimestre(nombre_archivo, n):
    
    f = open('cronograma_sugerido.csv', 'rt')
    filas = csv.reader(f)
    materias_sugeridas = []
    encabezado = next(filas)
    
    for fila in filas:
        if fila[0] == str(n):
            materias_sugeridas.append(dict(zip(encabezado, fila)))
    f.close()
    return materias_sugeridas

materias_cuatrimestre('cronograma_sugerido.csv', 3)