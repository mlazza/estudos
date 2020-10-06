#7. Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
# b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

def e07():

	p = int(input("Digite o valor do seu peso: "))
	p15 = p + p*15/100
	p20 = p - p*20/100

	print(f'O seu peso caso engorde 15% = {p15} \ncaso emagreça 20% = {p20}')


if(__name__ == "__main__"):
    e07()
