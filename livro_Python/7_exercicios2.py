#7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
#ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
#de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
#ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
#dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
#informe-lhes o preço do ingresso do cinema.

cond = True

while cond:

    idade = input("Qual é a idade? q=sair")
    
    if idade == 'q':
        cond = False
    
    else:
        idade = int(idade)

        if idade < 3:
           print("Ingresso gratuito")
        elif idade <= 12:
            print("Ingresso: $10")
        elif idade > 12:
            print("Ingresso: $15")

#7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
#7.5 que faça o seguinte, pelo menos uma vez: • use um teste condicional na
#instrução while para encerrar o laço; • use uma variável active para controlar
#o tempo que o laço executará; • use uma instrução break para sair do laço
#quando o usuário fornecer o valor 'quit'.


active = True

while active:

    idade = input("Qual é a idade? q=sair")
    
    if idade == 'q':
        break
    
    else:
        idade = int(idade)

        if idade < 3:
           print("Ingresso gratuito")
        elif idade <= 12:
            print("Ingresso: $10")
        elif idade > 12:
            print("Ingresso: $15")


#7.7 – Infinito: Escreva um laço que nunca termine e execute-o. (Para encerrar #o laço, pressione CTRL-C ou feche a janela que está exibindo a saída.)

active = True
n = 1

while active:
    
    print(n)
    n+=1
    #LOOP INFINITO