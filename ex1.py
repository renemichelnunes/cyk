from cyk import cyk, regra

c = cyk() #ababc

S = regra('S', ['aXc'])
X = regra('X', ['aX'])
X = regra('X', ['bX'])
X = regra('X', ['cX'])
X = regra('X', [])

detalhes = True

c.testa_palavra('ababc')


