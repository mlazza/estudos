#5.1 Testes condicionais - Escreva uma serie de testes condicionais
# Exiba a frase que descreva o testo e o resultado previsto p cada um
# car = 'subaru' print('Is car == subaru? I predict True') print(car == 'subaru'), p.e.

car = 'subaru'
car2 = 'nissan'

print("O carro é um subaru? Acho que sim!")
print(car=='subaru')

print("O carro é um Corola? Eu acho que não!")
print(car2=='corola')

print("Criando uma lista de carros...")
lista = ['subaru', 'chevrolet', 'fiat', 'nissan', 'vw']

print("O carro ferrari está na lista? Eu não sei...")

print("Testando")
print('ferrari' in lista)

print("Testando o subaru")
print('subaru' in lista)

print("A lista:")
for carro in lista:
	print("\t" + carro)