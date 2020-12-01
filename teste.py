# -*- coding: utf-8 -*-
# Use a versão 3 ou superior do python

from cyk import regra, cyk

gramatica = []
with open ('gramatica.txt', 'r') as reader:
    for linha in reader:
        a = linha.split()
        a.remove('=>')
        a.remove('|')
        gramatica.append(a)

c = cyk()
for i in gramatica:
    a = i.pop(0)
    reg = regra(a, i)
    c.incluir_regra(reg)

c.testa_palavra('baaba')   
c.testa_palavra('baabaa')   
