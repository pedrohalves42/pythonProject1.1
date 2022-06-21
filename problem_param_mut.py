def lista_de_Clientes(clientes_interaviel, lista=None):
    if lista is None:
        lista= []
    lista.extend(clientes_interaviel)
    return lista

lista_de_Clientes_1 = ['Paulo']
cliente1 = lista_de_Clientes(['joao', 'maria', 'eduardo'],lista_de_Clientes_1)
cliente2 = lista_de_Clientes(['Marcos','Jonas','Zico'])
cliente3 = lista_de_Clientes(['Maria','fabricio','pedro'])


print(cliente1)
print(cliente2)
print(cliente3)