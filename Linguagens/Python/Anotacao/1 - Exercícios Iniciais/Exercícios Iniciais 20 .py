# -*- coding: utf-8 -*-
"""
Ex: Três massas m1, m2 e m3 estão separadas por distâncias r12, r13, r23, como mostra a figura.
Se G é a constante de gravitação universal, a força de coesão para manter a massa das partículas juntas é dada pela fórmula:
F = G.[ (m1.m2)/r122 + (m1.m3)/r132 + (m2.m3)/r232 ]
"""

m1 = float(input('Digite massa 1: '))
m2 = float(input('Digite massa 2: '))
m3 = float(input('Digite massa 3: '))
r12 = float(input('Digite distância 1: '))
r13 = float(input('Digite distância 2: '))
r23 = float(input('Digite distância 3: '))

G = float(6.67 * 10**-11)

F = float(G * ((m1 * m2)/r12**2 + (m1 + m3)/r13**2 + (m2 * m3)/r23**2))

print(f'O valor é: {F:.20f}')