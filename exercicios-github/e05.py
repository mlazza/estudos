#5. Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
# que este sofreu um desconto de 10%.

def e05():

	p1 = int(input("Digite o valor do produto: "))
	
	print(f'O novo preço do produto é: {p1-p1*10/100}')

if(__name__ == "__main__"):
    e05()
