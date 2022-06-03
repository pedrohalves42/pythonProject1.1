'''
try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro desenvolvedor, fale com ele ')
except(IndexError, KeyError) as erro:
    print('Erro de Indice')
except Exception as erro:
    print('Ocorreu um erro inesperado ')
else:
    print('Seu codigo foi executado com sucesso')
    print(a)

finally:
    print('Finalmente ')

print('Bora continuar....')
'''
try:
    a = 1/0
except NameError as erro:
    print('Erro desenvolvedor, fale com ele ')
except(IndexError, KeyError) as erro:
    print('Erro de Indice')
except Exception as erro:
    print('Ocorreu um erro inesperado ')
else:
    pass

finally:
    a = ''

print(a)