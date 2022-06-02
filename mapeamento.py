from map import pessoas, produtos, lista

'''
#nova_lista = map(lambda x: x * 2,lista)

nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))



def aumentar_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumentar_preco, produtos)
for produto in novos_produtos:
    print(produto)
'''


def aumento_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.05)
    return p


nomes = map(aumento_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
