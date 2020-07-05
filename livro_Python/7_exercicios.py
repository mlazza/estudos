#7.1 Locação de automoveis - pergunta ao usuario qual carro ele gostaria de alugar
# mostre msg sobre este carro, tipo "Deixe-me ver se consigo este 'car' pra voce"

carro = input("Qual carro voce gostaria de alugar?")

print("Vou verificar se encontro este " + carro.title() + " pra voce!")

#7.2 Lugares no restaurante - pergunta ao usuario quantas pessoas pra mesa. Se > 8 exiba msg
# dizendo que eles deverao esperar uma mesa, senao informe que a mesa esta pronta

pessoas = int(input("Quantos lugares vocês precisam?"))

if pessoas > 8:
	print("Não tem espaço pra tudo isso, rapaiz")
else:
	print("Podem ir até a mesa 332, por favor!")

#7.3 Multiplos de 10 - peca ao usuario um numero e em seguida informe se é ou nao multiplo de 10

numero = int(input("Informe um numero: "))

if numero % 10 == 0:
	print("Seu numero é multiplo de 10")
else:
	print("Seu numero não é multiplo de 10")

#7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
#fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
#fornecido. À medida que cada ingrediente é especificado, apresente uma
#mensagem informando que você acrescentará esse ingrediente à pizza.

pizza = []
cond = True

while cond == True:
    
    print("Ingredientes escolhidos: ")
    for p in pizza:
        print("\t" + p)

    print("Forneça o ingrediente para a pizza: [quit para sair]")
    ingrediente = input()
    


    if (ingrediente == 'quit'):
        cond = False
    else:
        pizza.append(ingrediente)
        print("Acrescentando " + ingrediente + " na pizza.")


