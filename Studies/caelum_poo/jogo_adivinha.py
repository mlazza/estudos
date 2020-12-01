# JOGO DA ADIVINHACAO

def jogar():

    print('***************************************')
    print('***Bem vindo ao jogo da Adivinhacao!***')
    print('***************************************')

    num_secreto = 42
    total_tentativas = 3

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))

        chute = int(input('Digite um numero: '))
        print('Você digitou ', chute)

        acertou = num_secreto == chute
        maior = chute > num_secreto
        menor = chute < num_secreto

        if (acertou):
            print('Você acertou!')
            break
        elif(maior):
            print('Você errou. Seu chute foi maior')
        elif(menor):
            print('Você errou. Seu chute foi menor')
