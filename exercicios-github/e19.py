#19. sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 W
# de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre
# a sua área (em m2) e a potência de iluminação que deverá ser utilizada.

def e19():

	med1 = int(input("Digite a primeira medida: "))
	med2 = int(input("Digite a segunda medida: "))
	area = med1 * med2
	iluminar_bem = 18

	print(f"A sua área do comodo é de {area} metros quadrados")
	print(f'O valor para a potencia a ser utilizada é de: {iluminar_bem*area} W')

if(__name__ == "__main__"):
    e19()
