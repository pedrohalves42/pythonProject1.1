def master(funcao):
    def slave():
        print('Oi')

    return slave


def fala_oi():
    print('Oi')


variavel = master(fala_oi())
variavel()
