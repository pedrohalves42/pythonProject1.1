'''
with open('abc.txt','w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())
'''
import json
d1 = {
    'Pessoa 1 ':{
        'nome':'Luiz',
        'idade': 25,

    },
    'Pessoa 2':{
        'nome':'Luiz',
        'idade': 30,
    },
}
d1_json = json.dumps(d1)
with open('abc.json','w+')as file:
    file.write(d1_json)


