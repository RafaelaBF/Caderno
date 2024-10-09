# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 8

Faça um programa que leia 100 números inteiros e diga quantos são ímpares.
"""
quant = 0

for i in range(1, 101):
    n = float(input('Entre com um número: '))
    if n%2 == 1:
        quant += 1
        
print (f'{quant} são ímpares')