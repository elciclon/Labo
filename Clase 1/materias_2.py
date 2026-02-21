#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:59:17 2026

@author: adrian
"""
import csv

def cuantas_materias(n):
    counter = 0
    f = open('cronograma_sugerido.csv', 'rt')
    filas = csv.reader(f)
    
    for fila in filas:
        if fila[0] == str(n):
            counter += 1
    f.close()
    return counter

cuantas_materias(5)