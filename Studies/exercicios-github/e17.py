#17. Faça um programa que receba o raio, calcule e mostre:
# a) o comprimento de uma esfera; sabe-se que c = 2 * p R;
# b) a área de uma esfera; sabe-se que A = p R2;
# c) o volume de uma esfera; sabe-se que v = ¾ * p R3.

def e17():

	raio = int(input("Digite o valor do raio: "))
	pi = 3.14
	comp = 2 * pi * raio
	area = pi * raio**2
	vol = 3/4 * pi * raio**3

	print(f'O valor do comprimento é {comp}')
	print(f'O valor da area é {area}')
	print(f'O valor do volume é {vol}')

if(__name__ == "__main__"):
    e17()
