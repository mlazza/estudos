
#16. Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
import math
def e16():

	cat1 = int(input("Digite o primeiro cateto: "))
	cat2 = int(input("Digite o segundo cateto: ")) 
	hip = math.sqrt(cat1**2 + cat2**2)


	print(f'O resultado do valor da hipotenusa é {hip}')

if(__name__ == "__main__"):
    e16()
