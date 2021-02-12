# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:21:13 2021

@author: Nikita
"""
from string import Template
import numpy as np

template_line = """   <line stroke="$color" opacity="1" x1="$x1" y1="$y1" x2="$x2" y2="$y2" stroke-width="1.6"/>\n"""
template_line = Template(template_line)

secret_message = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def messageWriteA(start_row : int, end_row : int, start_col : int, end_col : int):
    A = [[0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = A[i - start_row][j - start_col]

def messageWriteB(start_row : int, end_row : int, start_col : int, end_col : int):
    B = [[0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = B[i - start_row][j - start_col]

def messageWriteC(start_row : int, end_row : int, start_col : int, end_col : int):
    C = [[0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = C[i - start_row][j - start_col]

def messageWriteD(start_row : int, end_row : int, start_col : int, end_col : int):
    D = [[0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = D[i - start_row][j - start_col]

def messageWriteE(start_row : int, end_row : int, start_col : int, end_col : int):
    E = [[0, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = E[i - start_row][j - start_col]

def messageWriteG(start_row : int, end_row : int, start_col : int, end_col : int):
    G = [[0, 0, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = G[i - start_row][j - start_col]

def messageWriteH(start_row : int, end_row : int, start_col : int, end_col : int):
    H = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = H[i - start_row][j - start_col]

def messageWriteI(start_row : int, end_row : int, start_col : int, end_col : int):
    I = [[0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = I[i - start_row][j - start_col]

def messageWriteJ(start_row : int, end_row : int, start_col : int, end_col : int):
    J = [[0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = J[i - start_row][j - start_col]

def messageWriteK(start_row : int, end_row : int, start_col : int, end_col : int):
    K = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = K[i - start_row][j - start_col]

def messageWriteF(start_row : int, end_row : int, start_col : int, end_col : int):
    F = [[0, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = F[i - start_row][j - start_col]

def messageWriteL(start_row : int, end_row : int, start_col : int, end_col : int):
    L = [[0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = L[i - start_row][j - start_col]

def messageWriteM(start_row : int, end_row : int, start_col : int, end_col : int):
    M = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = M[i - start_row][j - start_col]

def messageWriteN(start_row : int, end_row : int, start_col : int, end_col : int):
    N = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = N[i - start_row][j - start_col]

def messageWriteO(start_row : int, end_row : int, start_col : int, end_col : int):
    O = [[0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = O[i - start_row][j - start_col]

def messageWriteP(start_row : int, end_row : int, start_col : int, end_col : int):
    P = [[0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = P[i - start_row][j - start_col]

def messageWriteQ(start_row : int, end_row : int, start_col : int, end_col : int):
    Q = [[0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Q[i - start_row][j - start_col]

def messageWriteR(start_row : int, end_row : int, start_col : int, end_col : int):
    R = [[0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = R[i - start_row][j - start_col]

def messageWriteS(start_row : int, end_row : int, start_col : int, end_col : int):
    S = [[0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = S[i - start_row][j - start_col]

def messageWriteT(start_row : int, end_row : int, start_col : int, end_col : int):
    T = [[0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = T[i - start_row][j - start_col]

def messageWriteU(start_row : int, end_row : int, start_col : int, end_col : int):
    U = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = U[i - start_row][j - start_col]

def messageWriteV(start_row : int, end_row : int, start_col : int, end_col : int):
    V = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = V[i - start_row][j - start_col]

def messageWriteW(start_row : int, end_row : int, start_col : int, end_col : int):
    W = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = W[i - start_row][j - start_col]

def messageWriteY(start_row : int, end_row : int, start_col : int, end_col : int):
    Y = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Y[i - start_row][j - start_col]

def messageWriteX(start_row : int, end_row : int, start_col : int, end_col : int):
    X = [[0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = X[i - start_row][j - start_col]

def messageWriteZ(start_row : int, end_row : int, start_col : int, end_col : int):
    Z = [[0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Z[i - start_row][j - start_col]

def messageWriteSh(start_row : int, end_row : int, start_col : int, end_col : int):
    Sh = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Sh[i - start_row][j - start_col]

def messageWriteTz(start_row : int, end_row : int, start_col : int, end_col : int):
    Tz = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Tz[i - start_row][j - start_col]
            
def messageWriteSpace(start_row : int, end_row : int, start_col : int, end_col : int):
    Space = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    for i in range(start_row, end_row+1):
        for j in range (start_col,end_col+1):
            secret_message[i][j] = Space[i - start_row][j - start_col]

messageWriteSpace(2,8,15,21) 
messageWriteSpace(2,8,85,91) 
messageWriteSpace(2,8,57,63) 
messageWriteA(2,8,8,14) 
messageWriteA(2,8,120,126) 
messageWriteA(2,8,64,70) 
messageWriteE(2,8,106,112) 
messageWriteF(2,8,113,119) 
messageWriteI(2,8,50,56) 
messageWriteI(2,8,78,84) 
messageWriteL(2,8,36,42) 
messageWriteL(2,8,1,7) 
messageWriteM(2,8,22,28) 
messageWriteN(2,8,127,133) 
messageWriteN(2,8,71,77) 
messageWriteSh(0,10,92,98) 
messageWriteT(2,8,99,105) 
messageWriteTz(0,10,43,49) 
messageWriteU(2,8,29,35) 

secret_message.reverse()
for line in secret_message:
    line.reverse()

width = 10.0
height= 10.0
square_origin_x = 200.0
square_origin_y = 200.0
square_end_x = square_origin_x + 2*135*width 
square_end_y = square_origin_y + 11*3*height

def getPoint(division_length : float, x : int, y : int, x_origin : float, y_origin : float):
    return [x_origin + 2*x*division_length, y_origin + 3*y*division_length]

def drawRectangle(division_length_x : float, division_length_y : float, origin_x : float, origin_y : float, divisions_x : int, divisions_y : int):
    color_black = "#000"
    final_x = origin_x + division_length_x*divisions_x
    final_y = origin_y + division_length_y*divisions_y
    for i in range(0,divisions_x):
        start_x = origin_x + i*division_length_x
        next_x = origin_x + (i+1)*division_length_x
        lines_file.write(template_line.substitute(x1 = start_x, x2 = next_x, y1 = origin_y, y2 = origin_y, color = color_black))
        lines_file.write(template_line.substitute(x1 = start_x, x2 = next_x, y1 = final_y, y2 = final_y, color = color_black))
    
    for i in range(0,divisions_y):
        start_y = origin_y + i*division_length_y
        next_y = origin_y + (i+1)*division_length_y
        lines_file.write(template_line.substitute(x1 = origin_x, x2 = origin_x, y1 = start_y, y2 = next_y, color = color_black))
        lines_file.write(template_line.substitute(x1 = final_x, x2 = final_x, y1 = start_y, y2 = next_y, color = color_black))
        
def drawDiamond(division_length : float, origin_x, origin_y):
    color_red = "#F00"
    color_blue = "#00F"
    west  = [origin_x , origin_y + division_length]
    north = [origin_x + division_length , origin_y]
    east  = [origin_x + 2*division_length , origin_y + division_length]
    south = [origin_x + division_length , origin_y + 2*division_length]
    center= [origin_x + division_length , origin_y + division_length]
    ssouth = [origin_x + division_length , origin_y + 3*division_length]

    lines_file.write(template_line.substitute(x1 = west[0], x2 = north[0] , y1 = west[1] , y2 = north[1] , color = color_blue ))
    lines_file.write(template_line.substitute(x1 = north[0], x2 = east[0] , y1 = north[1] , y2 = west[1] , color = color_blue ))
    lines_file.write(template_line.substitute(x1 = west[0] , x2 = south[0] , y1 = west[1] , y2 = south[1] , color = color_red ))
    lines_file.write(template_line.substitute(x1 = south[0] , x2 = east[0] , y1 = south[1] , y2 = east[1] , color = color_red))
    lines_file.write(template_line.substitute(x1 = center[0] , x2 = south[0] , y1 = center[1] , y2 = south[1] , color = color_blue))
    lines_file.write(template_line.substitute(x1 = north[0] , x2 = center[0] , y1 = north[1] , y2 = center[1] , color = color_red))
    lines_file.write(template_line.substitute(x1 = south[0] , x2 = ssouth[0] , y1 = south[1] , y2 = ssouth[1] , color = color_blue))
    
def drawConnectingLine(division_length : float, origin_x, origin_y):
    color_red = "#F00"
    color_blue = "#00F"
    north = [origin_x + division_length , origin_y]
    center= [origin_x + division_length , origin_y + division_length]    
    south = [origin_x + division_length , origin_y + 2*division_length]
    ssouth = [origin_x + division_length , origin_y + 3*division_length]
    lines_file.write(template_line.substitute(x1 = north[0] , x2 = center[0] , y1 = north[1] , y2 = center[1] , color = color_blue))
    lines_file.write(template_line.substitute(x1 = center[0] , x2 = south[0] , y1 = center[1] , y2 = south[1] , color = color_red))
    lines_file.write(template_line.substitute(x1 = south[0] , x2 = ssouth[0] , y1 = south[1] , y2 = ssouth[1] , color = color_blue))

def generateLines(divisions_x : int, divisions_y : int, x1 : float, x2:float, y1:float, y2:float):
    color_red = "#F00"
    color_blue = "#00F"
    color_magenta = "#F0F"
    square_height = y2 - y1
    division_length = square_height/divisions_y
    offset = 2
    for i in range(1,divisions_y):
        line_y = y1 + i*division_length
        if ((i+offset)% 3 == 0):    
            lines_file.write(template_line.substitute(x1 = x1, x2 = x2, y1 = line_y, y2 = line_y,color = color_red))
        elif((i+offset)%3 == 1):
            lines_file.write(template_line.substitute(x1 = x1, x2 = x2, y1 = line_y, y2 = line_y,color = color_blue))
            
    for i in range(1,divisions_x):
        line_x = x1 + i*division_length
        for j in range(0,divisions_y):
            line_y = y1 + j*division_length
            if (i%2 == 0):
                if (j%3 == 0):
                    lines_file.write(template_line.substitute(x1 = line_x, x2 = line_x, y1 = line_y, y2 = line_y+division_length,color = color_red))
                elif(j%3 == 1):
                    lines_file.write(template_line.substitute(x1 = line_x, x2 = line_x, y1 = line_y, y2 = line_y+division_length,color = color_blue))
                elif(j%3 == 2):
                    lines_file.write(template_line.substitute(x1 = line_x, x2 = line_x, y1 = line_y, y2 = line_y+division_length,color = color_red))

start = """
<svg width="2000" height="2000" xmlns="http://www.w3.org/2000/svg">
 <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->

 <g>
  <title>background</title>
  <rect fill="#fff" id="canvas_background" height="10000" width="10000" y="-1" x="-1"/>
  <g display="none" id="canvasGrid">
   <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%" width="100%" id="svg_3"/>
  </g>
 </g>
 <g>
  <title>Layer 1</title>
"""
end = """
 </g>
</svg>
""".format(square_end_x - square_origin_x, square_end_y - square_origin_y)
            
divisions_x = int((square_end_x - square_origin_x)/width)
divisions_y = int((square_end_y - square_origin_y)/height)
lines_file = open("SimulateMe.svg", "w")
lines_file.write(start)
division_length = (square_end_x - square_origin_x)/divisions_x

generateLines(divisions_x,divisions_y, square_origin_x, square_end_x, square_origin_y, square_end_y)

secret_x = len(secret_message[0])
secret_y = len(secret_message)

for i in range(0,secret_y):
    for j in range (0,secret_x):
        point = getPoint(division_length, x = j, y = i, x_origin = square_origin_x, y_origin = square_origin_x)
        if (secret_message[i][j] == 1):
            drawDiamond(division_length, point[0], point[1])
        else:
            drawConnectingLine(division_length, point[0], point[1])

drawRectangle( division_length, division_length, square_origin_x, square_origin_y, divisions_x, divisions_y )
lines_file.write(end)
lines_file.close()

"""
For a 48 by 48 square, there are precisely 24 X starting points and 16 Y starting
points. That means that there are precisely 384 diamonds that can be drawn.
Starting points along X are at x_origin, x_origin + 2*division_length... x_origin + 23* division_length
starting points along Y are at y_origin, y_origin + 3*division_lenght... y_origin + 3*15*division_length
"""

"""
msg = "REDACTED"
temp = Template(" messageWrite$letter(2,8,$val1,$val2) )
for i in range(0,len(msg)):
    print(temp.substitute(letter = msg[i], val1 = 7*i + 1, val2 = 7*i + 7 ))
"""

instructions = """
1. First of all, visit https://origamisimulator.org/ 

2. Take a moment to appreciate the genius of the people who built this.

3. Enough already? Alrite alrite, maybe try sliding the little bar at the
bottom of the screen. See what happens when the model is fully folded. 

4. You can even view how tense the paper is, just switch from the "Material"
view to the "Strain" view. Cool? I bet. Now revert back to the material view.

5. Maybe try rotating the model around for a bit.

6. Alright, awesome, I think you're ready. Refresh the page for now, don't rotate
anything and make sure that the slider is pointing towards "Flat".

8.See that small "SimulateMe.svg" file? Great, put it somewhere handy.

9. Click on the "File" menu, then click on "Import... (SVG/FOLD)". Import the 
"SimulateMe.svg". The process might take a while (could take a minute on an 
 older computer).

10. DO THIS SLOWLY : gradually increase the fold percentage to 60 percent.
Don't rush it, the paper will start oscillating like crazy otherwise.

11. Click on the "View" menu, then "View Direction >" and then "View Top".

12. Finally, click on "View", then "Rotate Model >" and then on "Rotate Around Z".

13. ...

14. Profit!!
"""

readme_file = open("INSTRUCTIONS_README.txt","w")
readme_file.write(instructions)
readme_file.close()
