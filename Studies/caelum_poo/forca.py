import random

#Função Main
def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while(not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        print(letras_acertadas)
        print('Erros:', erros)

        acertou = '_' not in letras_acertadas
        enforcou = erros == 6

    mensagem_final(acertou, palavra_secreta)

#Funções complementares
def mensagem_final(acertou, palavra):

    if(acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu')
        print('A palavra era {}'.format(palavra))

    print('Fim do jogo.')

def mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras(palavra):

    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual letra?')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1
