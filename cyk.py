'''
Copyright (C) <2020>  <René Michel de A. M. Nunes>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
class regra():
    def __init__(self, nome, sentenca):
        self.nome = nome
        self.sentenca = sentenca

class cyk():
    def __init__(self):
        self.gramatica = []
        self.detalhes = False
    
    def incluir_regra(self, r):
        if self.gramatica == []:
            self.gramatica.append(r)
            if self.detalhes:
                print('regra {} adicionada'.format(r.nome))
        else:
            for i in self.gramatica:
                if r.nome == i.nome:
                    print('a regra {} já existe'.format(r.nome))
                    return False
            self.gramatica.append(r)
            if self.detalhes:
                print('regra {} adicionada'.format(r.nome))
        return True
    
    def imprime(self):
        print('Gramática:')
        for i in self.gramatica:
            print('{} -> {}'.format(i.nome, i.sentenca))
        print()

    def testa_palavra(self, palavra):
        self.imprime()
        def busca(item):
            lin = len(item) - 1
            if lin >= 0:
                for i in tabela2[lin]:
                    if i == item:
                        col = tabela2[lin].index(item)
                        return tabela3[lin][col]
        
        def verifica(a):
            temp = []
            for i in self.gramatica:
                for j in i.sentenca:
                    if a == j:
                        if i.nome not in temp:
                            temp.append(i.nome)
            return temp
        
        def calcula(a, b):
            temp = []
            for i in a:
                for j in b:
                    c = '{}{}'.format(i, j)
                    d = verifica(c)
                    if d not in temp and d != []:
                        temp += d
            return temp

        def testa():
            a = tabela3[len(tabela3) - 1][0]
            for i in a:
                if i == self.gramatica[0].nome:
                    return True
            return False

        # Primeira linha da matriz
        linha = []
        for i in range(0, len(palavra)):
            temp = []
            for j in self.gramatica:
                if palavra[i] in j.sentenca:
                    if j.nome not in temp:
                        temp.append(j.nome)
            temp.sort()
            linha.append(temp)

        # Criando tabela guia
        tabela2 = []
        for i in range(1, len(palavra) + 1):
            pi = 0
            pf = i
            temp = []
            for j in range(0, len(palavra)):
                subpal = palavra[pi:pf]
                temp.append(subpal)
                pi += 1
                pf += 1
                if pf > len(palavra):
                    break
            tabela2.append(temp)
        if self.detalhes:
            print('tabela2')
            for i in tabela2:
                print(i)
            print()

        # Montando a tabela de resultado
        tabela3 = tabela2.copy()
        tabela3[0] = linha
        
        for i in range(1, len(tabela2)):
            linha = []
            for j in range(0, len(tabela2[i])):
                index = 1
                temp = []
                temp2 = []
                while index < len(tabela2[i][j]):
                    inicio = tabela2[i][j][0:index]
                    resto = tabela2[i][j][index:]
                    if self.detalhes:
                        print('inicio={} resto={}'.format(inicio, resto))
                    v1 = busca(inicio)
                    v2 = busca(resto)
                    if self.detalhes:
                        print('v1={} v2={}'.format(v1, v2))
                    v3 = calcula(v1, v2)
                    if self.detalhes:
                        print('v3={}'.format(v3))
                    for a in v3:
                        if a not in temp2:
                            temp2.append(a)
                    #print('temp2={}'.format(temp2))
                    index += 1
                    if self.detalhes:
                        print()
                temp += temp2
                if self.detalhes:
                    print('temp={}'.format(temp))
                linha.append(temp)
                if self.detalhes:
                    print('linha={}'.format(linha))
            tabela3[i] = linha
            if self.detalhes:
                print()
        print('Tabela CYK:')
        for i in tabela3:
            print(i)
        print()

        if testa():
            print('palavra "{}" pertence à gramática'.format(palavra))
        else:
            print('palavra "{}" não pertence à gramática'.format(palavra))
