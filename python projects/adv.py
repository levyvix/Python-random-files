import random

magico = random.randint(1, 20)
print(magico)
# Quantidade de chances:
def jogoNovo():
    arq = open('maior.txt', 'r+')
    maior = int(arq.read(1))
    # Apresentação do jogo:
    print('Bem vindo ao Adivinhe o Número!')
    print('O número mágico é um numero de 1 a 20. Tente descobrir qual é!')
    print('O recorde atual é de {} tentativas. Consegue adivinhar o número com menos tentativas?'.format(maior))
    arq.close()
    tentativas = 0
    while True:

        print('\n\nFaca seu chute: ')
        guess = int(input(''))

        # Verificando se acertou:
        if guess == magico:
            # Verificando se é novo recorde:
            if tentativas < maior:
                print('\nVoce acertou o numero! Com {} tentativas! Um novo recorde!'.format(tentativas))
                # Abre no modo escrita, pra reescrever o recorde atual
                arq = open('maior.txt', 'w')
                arq.write(str(tentativas))
                arq.close()
                break
            else:
                # Acertou, mas nao foi recorde
                print('\nVocê acertou o número! Com {} tentativas, o recorde são com {} tentativas!'.format(tentativas, maior))
                break
        else:
            # Se errar perde uma vida
            tentativas += 1
            # Se vida chegar a zero, perdeu
            print('\nVocê errou o numero!')
            print('Você já tentou acertar {} vezes!'.format(tentativas))

jogoNovo()