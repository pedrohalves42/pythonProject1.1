'''
zip - unindo iteraveis
zip_longest - itertools

'''
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador ', 'Monte belo', 'Arcos']

estados = ['SP', 'MG', 'BA', 'MG']

cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')

# print(next(cidades_estados))
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

# for valor in cidades_estados:
#    print(valor)
