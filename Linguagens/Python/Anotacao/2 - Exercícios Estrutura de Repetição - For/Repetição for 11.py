# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 11

Faça um programa que leia um número inteiro e 
calcule e mostre os n primeiros termos da série de Fibonacci. 

for i in range(1, n+1):
    if i <= 2 :
        f.append(1)
    else:
        x = f[i] + f[i]
        f.append(x)
"""

n = int(input('Entre com um número: '))
f = []


for i in range(1, 3):
    if i <= 2 :
        f.append(1)

for i in range(2, n):
    x = f[i-1] + f[i-2]
    f.append(x)
        
print(f)