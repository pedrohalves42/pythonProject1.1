perguntas = {
    'pergunta 1 ': {
        'pergunta': 'Quanto e 2 + 2 ',
        'respostas': {'a': '1', 'b': '2', 'c': '4'},
        'resposta_certa': 'c',
    },
    'pergunta 2 ': {
        'pergunta': 'Quanto e 2 * 9',
        'respostas': {'a': '18', 'b': '24', 'c': '42'},
        'resposta_certa': 'a',
    },
}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha as opções abaixo:')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')

    resposta_user = input('Sua resposta:')
    print(f' A sua resposta foi: {resposta_user}')
    if resposta_user == pv['resposta_certa']:
        print('ESTA CERTO PARABEEEEENS !!!!')
        respostas_certas += 1
    else:
        print('Você errou tente novamente')

qtd_pergunta = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_pergunta * 100
print(f'Você respondeu {qtd_pergunta} perguntas e acertou {respostas_certas}  ')
print(f'Sua porcentagem em acertos foi de {porcentagem_acerto}%')