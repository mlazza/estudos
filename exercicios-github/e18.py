#18. Faça um programa que receba uma temperatura em celsius, calcule e mostre essa temperatura em
# Fahrenheit. sabe-se que F = 180*(c + 32)/100.

def e18():

	temp = int(input("Digite o valor da temperatura em Celsius: "))
	celsius_to_fahr = 180 * (temp + 32) / 100

	print(f'O valor da temperatura em Fahrenheit é {celsius_to_fahr} F')

if(__name__ == "__main__"):
    e18()
