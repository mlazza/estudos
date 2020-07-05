#9. Faça um programa que calcule e mostre a área de um trapézio.
# sabe-se que: A = ((base maior + base menor) * altura)/2
def e09():

	b_maior = int(input("Digite o valor da base maior: "))
	b_menor = int(input("Digite o valor da base menor: "))
	altura = int(input("Digite o valor da altura: "))
	area = ((b_maior+b_menor)*altura)/2

	print(f'A área do trapézio é: {area}')


if(__name__ == "__main__"):
    e09()
