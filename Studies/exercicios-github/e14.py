#14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas.

def e14():

	ano_nasc = int(input("Digite o ano de nascimento: "))
	ano_agora = 2020 

	print(f'A idade da pessoa é: {ano_agora-ano_nasc} anos')
	print(f'A idade da pessoa é: {(ano_agora - ano_nasc)*12} meses')
	print(f'A idade da pessoa é: {(ano_agora - ano_nasc)*365} dias')
	print(f'A idade da pessoa é: {(ano_agora - ano_nasc)*1642} semanas')
	
if(__name__ == "__main__"):
    e14()
