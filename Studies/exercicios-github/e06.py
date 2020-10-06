#6. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
# que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
# salário final.

def e06():

	s1 = int(input("Digite o valor do salario: "))
	vendas = int(input("Digite o total de vendas: "))
	comissao = 4/100 * vendas

	print(f'Salario final: {s1+comissao} \nComissao: {comissao}')

if(__name__ == "__main__"):
    e06()
