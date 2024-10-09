# -*- coding: utf-8 -*-
"""
@author: Rafaela BF
 
Questão 1

Faça um programa que mostre a tabuada de 1 até 10 de um número inteiro lido 
do teclado. O resultado deve aparecer da seguinte forma: 
Se o número lido for 5.
    1 x 5 = 5
    2 x 5 = 10
        ...
    10 x 5 = 50
"""

n = int(input("Insira um número: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
