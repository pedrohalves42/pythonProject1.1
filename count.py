'''
count - itertools
'''

from itertools import count

'''
contador = count(start=1, step=3)

for valor in contador:
    print(round(valor,2))

    if valor >= 100:
        break
'''
contador = count()
lista = ['Luis', 'Joao', 'Maria', 'Silva', 'Eduardo']
lista = zip(contador, lista)
print(list(lista))
