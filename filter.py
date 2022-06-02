from map import produtos, pessoas, lista

'''
nova_lista = filter(lambda x: x > 2, lista)
print(list(nova_lista))
'''

'''
def filtra(produto):
    if produto['preco'] > 20:
        return True


nova_lista = filter(filtra, produtos)
for produto in nova_lista:
    print(produto)
'''


def filtra(pessoa):
    if pessoa['idade'] > 18:
        return True


nova_lista = filter(filtra, pessoas)

for maior in nova_lista:
    print(maior)
