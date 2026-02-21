#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 18:53:44 2026

@author: adrian
"""
import numpy as np

def pisar_elemento(M,e):
    forma_matriz = M.shape
    for i in range(forma_matriz[0]):
        for j in range(forma_matriz[1]):
            if M[i][j] == e:
                M[i][j] = -1
    
    return M
    
    
M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
pisar_elemento(M, 2)