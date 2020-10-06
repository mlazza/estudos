#3. Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo
# segundo. sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar
# com validações.

def e03():

	n1 = int(input("Digite o primeiro número: "))
	n2 = int(input("Digite o segundo número: ")) 
	
	print(f'O resultado de {n1} : {n2} é {n1/n2}')

if(__name__ == "__main__"):
    e03()
