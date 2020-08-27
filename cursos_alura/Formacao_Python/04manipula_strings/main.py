"""
sobreMim = "Meu nome é Rodrigo e minha idade é 26"
#meuNome = "Rodrigo"
#............0123456
subString = sobreMim[35:]
print(subString)
"""
'''
url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

argumento = "moedaorigem=real"
#............01234567890  
subString = argumento[5:11]
print(subString)
'''
'''
argumento = "moedaorigem=real"

lista_args = argumento.split("=")
print(lista_args)

index = argumento.find("=")
subString = argumento[index + 1:]
print(subString)
'''
"""
#None é diferente de vazio ''

string = ''

if string:
	print('Tem algo aqui')
else:
	print('Nao tem algo aqui')
"""

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "moedaorigem=real&moedadestino=dolar"
#url = None
#url = ''
argumentosUrl = ExtratorArgumentosUrl(url)
#print(argumento)
#print(ExtratorArgumentosUrl.urlEhValida(url))

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()

print(moedaDestino, moedaOrigem)