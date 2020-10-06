# 13. Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.
# Exemplo:
# Digite um número: 5
# 5 × 0 = 0
# 5 × 1 = 5
# 5 × 2 = 10
# 5 × 3 = 15
# 5 × 4 = 20
# 5 × 5 = 25
# 5 × 6 = 30
# 5 × 7 = 35
# 5 × 8 = 40
# 5 × 9 = 45
# 5 × 10 = 50

def e13():

	num1 = int(input("Digite o numero que quer a tabuada: "))
	cont = 10

	for numero in range(10):
		print(f'{num1} x {numero} = {num1*numero}')

if(__name__ == "__main__"):
    e13()
