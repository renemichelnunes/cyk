# cyk
Classe em python 3 que testa palavras em gramáticas na forma normal de Chomsky

A classe 'cyk.py' pode ser utilizada da seguinte maneira:
- Atribuindo a uma variável a classe 'regra' cujos parâmetros são o nome da regra e uma lista de strings que representa os parâmetros. 
- Instanciando a classe 'cyk' a qual possui alguns métodos:
  - 'incluir_regra(regra)', basta passar uma regra como parâmetro, isso é adicionado à uma lista que representa a gramática.
  - 'imprime()', o qual lista a gramática.
  - 'testa_palavra(palavra)', testa uma string que representa a cadeia de simbolos a ser verificada pela gramática. Como resultado é impressa uma matriz que representa o teste da cadeia de símbolos sobre a gramática, assim como uma mensagem afirmando se a cadeia pertençe a gramática ou não.
  -'detalhes=True', uma variável usada para mostrar mais detalhes do processo.

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
S AB BC
A BA a
B CC b
C AB a
```
Onde 'S' é o identificador da regra e AB BC os parâmetros, por exemplo, S->AB|BC é escrito como 'A AB BC' separados por espaços. A classe sempre identifica o primeiro parâmetro como sendo o identificador da regra e assim por diante com 'A BA a' como (A->BA|a)...
Junto com a classe há um programa 'teste.py' o qual demonstra lendo uma gramática a partir de um arquivo de texto.
