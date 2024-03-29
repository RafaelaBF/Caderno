# -*- coding: utf-8 -*-
"""
@author: rafaela
"""

'''
8 - Faça um programa que leia seu nome e o escreva na tela.
9 - Faça um programa que leia seu nome e sua idade e escreva na tela.
10 - Faça um programa que leia seu nome, sua idade e sua altura e escreva na tela.
'''

nome = str(input('Digita seu nome: '))
idade = int(input('Digita sua idade: '))
alt = float(input('Digita sua altura em metros: '))

print(f"Seu nome é {nome}, sua idade é {idade} e sua altura é {alt :.2f} metros")