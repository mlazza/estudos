#12. Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule
# e mostre a quantidade de salários mínimos que esse funcionário ganha.

def e12():

	sm = int(input("Digite o valor do salario minimo: "))
	salario = int(input("Digite o valor do seu salário: ")) 

	print(f'O seu salário totaliza {salario/sm}')

if(__name__ == "__main__"):
    e12()
