#2. Faça um programa que receba três números, calcule e mostre a multiplicação desses números.

def e02():

	n1 = int(input("Digite o primeiro número: "))
	n2 = int(input("Digite o segundo número: ")) 
	n3 = int(input("Digite o terceiro número: ")) 

	print(f'O resultado de {n1} x {n2} x {n3} é {n1*n2*n3}')

if(__name__ == "__main__"):
    e02()
