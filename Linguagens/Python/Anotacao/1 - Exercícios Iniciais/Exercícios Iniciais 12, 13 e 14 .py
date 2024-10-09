# -*- coding: utf-8 -*-
"""
@author: rafaela
"""
'''
12-Faça um programa que leia duas notas e imprima a média aritmética.
13-Faça um programa que leia duas notas e imprima a média aritmética arredondada.
14-Faça um programa que leia duas notas e imprima a média aritmética truncada.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f"A média aritmética entre {nota1} e {nota2} é {(nota1 + nota2)/2 :.2f}")

r = round((nota1 + nota2)/2)

print(f"E a média arrendondada é {r}")

print(f"A média aritmética truncada é {r}")