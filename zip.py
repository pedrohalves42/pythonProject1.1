'''
zip - unindo iteraveis
zip_longest - itertools

'''
cidades = ['São Paulo','Belo Horizonte', 'Salvador ','Monte belo']

estados = ['SP','MG','BA','MG']

cidades_estados = zip(estados,cidades)
#print(next(cidades_estados))

print(list(cidades_estados))
#for valor in cidades_estados:
#    print(valor)
