# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
carta = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
n = 20
for i in range (0, n-1):
    for j in range (i+1, n):
        if carta[i]<carta[j]:
            continue
        else:
            temp=carta[i]
            carta[i]=carta[j]
            carta[j]=temp