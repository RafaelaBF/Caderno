# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 10

Faça um programa que leia um número inteiro e calcule o seu fatorial. 
"""

num = int(input('Entre com um número: '))
fat = 1

for i in range(1, num+1):
    fat = fat * i
    
print(fat)
    