# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:30:19 2021

@author: andrz

lista = [6,3,4]

x = 0 
i = 2
max = x
imax = i

n = 3



while lista[x] > lista[max]:
  
    max=x+1
    imax = i 
    i=i+1

    while i<=n:
        print(i)
        print(x)    
    # nie działa 
"""


import matplotlib.pyplot as plt



x = [4,4,7,21]

plt.plot(x, 'ro')

n = 4

print(x)

max = x[0]

imax = 0

i = 1

for i in range(1, n):
    if x[i]>max:
        max = x[i]
        imax = i
        
print(max)
print(imax)