'''
Combinations,Permutations e product - Itertools
Combinação - ordem não importa
Permutação - ordem importa
Ambos não repetem valores unicos
Produto - ordem importa e repete valores unicos
'''
from itertools import combinations, product, permutations

pessoa = ['ana','fabio','andre','maria','pedro','leticia','joao']
for grupo in combinations(pessoa,2):
    print(grupo)