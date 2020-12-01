# cyk
Classe em python 3 que testa palavras em gramáticas na forma normal de Chomsky

A classe 'cyk.py' pode ser utilizada da seguinte maneira:
- Atribuindo a uma variável a classe 'regra' cujos parâmetros são o nome da regra e uma lista de strings que representa os parâmetros. 
- Instanciando a classe 'cyk' a qual possui alguns métodos:
  - 'incluir_regra(regra)', basta passar uma regra como parâmetro, isso é adicionado à uma lista que representa a gramática.
  - 'imprime()', o qual lista a gramática.
  - 'testa_palavra(palavra)', testa uma string que representa a cadeia de simbolos a ser verificada pela gramática. Como resultado é impressa uma matriz que representa o teste da cadeia de símbolos sobre a gramática, assim como uma mensagem afirmando se a cadeia pertençe a gramática ou não.
  - 'detalhes=True', uma variável usada para mostrar mais detalhes do processo.

```
from cyk import regra, cyk

c = cyk()

S = regra('S', ['AB', 'BC'])
A = regra('A', ['BA', 'a'])
B = regra('B', ['CC', 'b'])
C = regra('C', ['AB', 'a'])

c.incluir_regra(S)
c.incluir_regra(A)
c.incluir_regra(B)
c.incluir_regra(C)

c.testa_palavra('baaba')
```

E nos dá a saída:

```
Gramática:
S -> ['AB', 'BC']
A -> ['BA', 'a']
B -> ['CC', 'b']
C -> ['AB', 'a']

Tabela CYK:
[['B'], ['A', 'C'], ['A', 'C'], ['B'], ['A', 'C']]
[['A', 'S'], ['B'], ['S', 'C'], ['A', 'S']]
[[], ['B'], ['B']]
[[], ['S', 'C', 'A']]
[['S', 'A', 'C']]

palavra "baaba" pertence à gramática
```
Ou lendo um arquivo de texto com a gramática declarada da seguinte forma:
gramatica.txt

```
S => AB | BC
A => BA | a
B => CC | b
C => AB | a
```
Onde 'S' é o identificador da regra e AB | BC os parâmetros.
Junto com a classe há um programa 'teste.py' o qual demonstra lendo uma gramática a partir de um arquivo de texto. O conteúdo é o seguinte:
```
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
```
Com o resultado:
```
~$ python3 teste.py 
Gramática:
S -> ['AB', 'BC']
A -> ['BA', 'a']
B -> ['CC', 'b']
C -> ['AB', 'a']

Tabela CYK:
[['B'], ['A', 'C'], ['A', 'C'], ['B'], ['A', 'C']]
[['A', 'S'], ['B'], ['S', 'C'], ['A', 'S']]
[[], ['B'], ['B']]
[[], ['S', 'C', 'A']]
[['S', 'A', 'C']]

palavra "baaba" pertence à gramática
Gramática:
S -> ['AB', 'BC']
A -> ['BA', 'a']
B -> ['CC', 'b']
C -> ['AB', 'a']

Tabela CYK:
[['B'], ['A', 'C'], ['A', 'C'], ['B'], ['A', 'C'], ['A', 'C']]
[['A', 'S'], ['B'], ['S', 'C'], ['A', 'S'], ['B']]
[[], ['B'], ['B'], []]
[[], ['S', 'C', 'A'], ['A', 'S']]
[['S', 'A', 'C'], ['B']]
[['B']]

palavra "baabaa" não pertence à gramática
```
