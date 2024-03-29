# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 9

Faça um programa que leia 100 números e diga:
quantos estão acima de 1000, 
quantos são iguais a 1000 
e quantos estão abaixo de 1000.
"""

quant_cima = 0
quant_igual = 0
quant_baixo = 0

for i in range(1, 101):
    n = float(input('Entre com um número: '))
    if n < 1000:
        quant_baixo += 1
    elif n == 1000:
        quant_igual += 1
    else:
        quant_cima += 1
        
print(f'{quant_cima} estão acima de 1000')
print(f'{quant_igual} são iguais a 1000')
print(f'{quant_baixo} estão abaixo de 1000')

