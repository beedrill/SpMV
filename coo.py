#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#COO format
A = np.array([[1,0,0,0,0],[0,0,2,0,3],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


def coo(matrix1, matrix2):
    rowNum = int(matrix1.shape[0])
    columnNum = int(matrix1.shape[1])
    Value = np.array([], dtype = int)
    Column = np.array([], dtype = int)
    Row = np.array([], dtype = int)
    temp = [[0] for j in range(rowNum)]
    Result = np.array([], dtype = int)


    for i in range(rowNum):
        for j in range(columnNum):
            if matrix1[i][j] != 0:
                Value = np.append(Value, matrix1[i][j])
                Column = np.append(Column, j)
                Row = np.append(Row, i)


    #COO kernel
    for i in range(len(Value)):
        temp[Row[i]] += Value[i] * matrix2[Column[i]]


    for i in range(len(temp)):
        Result = np.append(Result, temp[i])

    print ("COO result is:", Result)


coo(A, B)
