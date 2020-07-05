#11. Faça um programa que calcule e mostre a área de um losango. sabe-se que: A = (diagonal maior * diagonal menor)/2.

def e11():

	dmn = int(input("Digite a diagonal maior: "))
	dma = int(input("Digite a diagonal menor: ")) 

	print(f'O resultado da área do losango é: {(dmn*dma)/2}')

if(__name__ == "__main__"):
    e11()
