#4. Faça um programa que receba duas notas, 
# calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.

def e04():

	n1 = int(input("Digite a primeira nota: "))
	n2 = int(input("Digite a segunda nota: ")) 
	
	print(f'O resultado da média ponderada: {(n1*2+n2*3)/5}')

if(__name__ == "__main__"):
    e04()
