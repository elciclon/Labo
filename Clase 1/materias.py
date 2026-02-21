#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:59:17 2026

@author: adrian
"""
import csv

lista_materias = []
f = open('cronograma_sugerido.csv', 'rt')

filas = csv.reader(f)
for fila in filas:
    lista_materias.append(fila[1])

lista_materias.pop(0)
f.close()