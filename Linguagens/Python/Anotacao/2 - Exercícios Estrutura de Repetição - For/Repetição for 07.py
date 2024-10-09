# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 7

Faça um programa que leia 100 números inteiros e diga qual é o menor. 
"""
n = int(input('Entre com um número: '))
menor = n

for i in range(1, 100):
    n = int(input('Entre com um número: '))
    if n < menor:
        menor = n

print(f'O menor número digitado foi {menor}')
