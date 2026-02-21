#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:55:17 2026

@author: adrian
"""

with open('datame.txt', 'rt') as f:
    for linea in f:
        if "estudiante" in linea:
            print(linea)