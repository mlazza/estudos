#15. João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar
# multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de
# João.

def e15():

	conta1 = int(input("Digite a primeirca conta: "))
	conta2 = int(input("Digite a segunda conta: ")) 
	salario = int(input("Digite o salario: ")) 
	multa = 2/100
	multa_valor = conta1*multa + conta2*multa

	sal_liq = salario - conta1 - conta2 - multa_valor

	print(f'O salario que você ganhou é {salario}, mas como teve que pagar multa e boleto, sobrou {sal_liq}')

if(__name__ == "__main__"):
   	e15()
