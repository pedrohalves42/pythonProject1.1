'''
d1 = {'Str': 'valor',
      123: 'Outro valor',
      (1, 2, 3, 4): 'Tupla'}
print('Str' in d1)
print('valor' in d1.values())
print(d1)
d2 = dict(chave1='Valor_Chave', chave2='Outro_valor',chave3='Valor_qualquer')
print(d2)
print('-' * 20)
for k in d1:
    print(k)
print('-' * 20)
for v in d1.values():
    print(v)
print('-' * 20)
for i in d1.items():
    print(i)
print('-' * 20)
for k, v in d1.items():
    print(k, v)
'''
'''
clientes = {
    'cliente1': {
        'Nome' : 'Luiz',
        'Sobrenome' : 'Alves',

    },
    'cliente2': {
        'Nome' : 'Joao',
        'Sobrenome' : 'Moreira'

    }
}
for clientes_k,clientes_v in clientes.items():
    print(f'Exibindo {clientes_k} ')
    for dados_k,dados_v in clientes_v.items():
        print(f'\t{dados_k},{dados_v}')
'''
import copy

'''
d1 = {1: 'a', 2: 'b', 3: 'c','d':['Luiz','Otavio']}
v = d1.copy()
v[1] = 'Luiz'
print(d1)
print(v)
print(v['d'][0])
'''
'''
d1 = {1: 'a', 2: 'b', 3: 'c','d':['Luiz','Otavio']}
v = copy.deepcopy(d1)
v[1] = 'Luiz'
v['d'][0] = 'Joaozinho'
print(d1)
print(v)
print(v['d'][0])
'''

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
d1 = dict(lista)
print(d1)
