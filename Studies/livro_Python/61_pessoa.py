#6.1 Pessoa. Use dicionario p armazenar: nome, sobrenome, idade, cidade

pessoa = {}

pessoa['first_name'] = 'Jorge'
pessoa['last_name'] = 'Odiler'
pessoa['age'] = 33
pessoa['city'] = 'Camboriu'

for key, value in pessoa.items():
	print(key + ": " + str(value))

#6.2 favorite_numbers

fav_numbers = {}

fav_numbers['marcelo'] = '08'
fav_numbers['marlon'] = '04'
fav_numbers['rochelle'] = '33'
fav_numbers['aires'] = '10'

for key, value in fav_numbers.items():
	print("\n" + key.title() + ": " + value)


#6.3 Glossário

glossario = {}

glossario['dicionário'] = 'Uma lista de valores de correspondência dupla, com chave : valor'
glossario['tupla'] = 'Uma lista de valores imutáveis, que não podem sofrer alteração depois de criados'
glossario['laço'] = 'Um evento de repetição, podendo ser utilizado com os comandos for, while'
glossario['variável'] = 'Uma reserva de memória para um valor determinado'
glossario['lista'] = 'Um conjunto de valores que podem ser guardados dentro de uma variável'

for key, value in glossario.items():
	print("\n" + key.title())
	print("\t" + value)

#6.4 Glossário 2 - add + 5 termos

#6.5 Rios - Dicionario com 3 rios importantes e o país

rios = {}

rios['nilo'] = 'Egito'
rios['amazonas'] = 'Brazil'
rios['iguaçu'] = 'Estado de SC'

for k, v in rios.items():
	print('O rio ' + k.title() + " fica no " + v)


#6.6 Enquete - lingua favorita #lista no dicionário

favorite_languages = {
	'marlon': ['python', 'c++'], 'rochelle': ['Java'], 'caio': ['c++', 'java'],
	'benjamin': ['python', 'c'], 
}

for name, languages in favorite_languages.items(): 
	print("\n" +
		name.title() + "'s favorite languages are:") 
	
	for language in languages:
		print("\t" + language.title())

#6.7 Ex. 6.1 crie 2 novos dict e armazene os 3 numa lista chamada people. Percorra com o for a lista
# a medida que percorrer apresente todas as infos da pessoa

pessoa = {}
pessoa2 = {}
pessoa3 = {}


pessoa['first_name'] = 'Jorge'
pessoa['last_name'] = 'Odiler'
pessoa['age'] = 33
pessoa['city'] = 'Camboriu'

pessoa2['first_name'] = 'Luigi'
pessoa2['last_name'] = 'Atila'
pessoa2['age'] = 39
pessoa2['city'] = 'Itajai'

pessoa3['first_name'] = 'Mateus'
pessoa3['last_name'] = 'Silveira'
pessoa3['age'] = 23
pessoa3['city'] = 'Ilhota'

lista = [pessoa, pessoa2, pessoa3]

for pessoa in lista: 

	print(pessoa)

#6.8 Animais de estimação

pets = []

monstro = {'pitbull': 'Marcelo'}
mel = {'pintcher': 'Juliana'}
buiu = {'guaipeca': 'Fabio'}

pets.append(monstro)
pets.append(mel)
pets.append(buiu)

print(pets)

#6.9 - Lugares favoritos - dicionario fav_places = pessoa: lugar favorito

#6.10 - Numeros favoritos

fav_numbers = {}

fav_numbers['marcelo'] = ['08', '16', '56']
fav_numbers['marlon'] = ['04']
fav_numbers['rochelle'] = ['33', '02']
fav_numbers['aires'] = ['10', '12']

for key, values in fav_numbers.items():
	print("\n" + key.title() + ": ")

	for value in values:
		print(value)


#6.11 Cidades dic=cities Use o nome de 3 cidades como chaves do seu dict. Crie um dict com infos
#sobre cada cidade, inclua país, populacao aproximada e um fato da cidade. As chaves do dict de cada cidade devem
# ser algo como country - population - fact. Apresente o nome de cada cidade e todas as infos delas.

cities = {
	'porto uniao': {
		'país': 'Brazil', 'pop': '34551', 'fato': 'Realiza o festival do Xixo'
	},
	
	'paris': {
		'país': 'USA', 'pop': '26490', 'fato': 'Tem trilhas de mountain bike'
	},
	
	'sidney': {
		'país': 'Australia', 'pop': '5131326', 'fato': 'Alguns pontos turísticos são a Opera de Sydney , o museu de arte contemporanea e o edificio Queen Victoria'
	},
  }

for city, infos in cities.items():
  	print("A cidade de " + city.title() + " possui os seguintes dados: ")
  	print("\tEstá localizado no " + infos['país'])
  	print("\tA sua população é estimada em " + infos['pop'])
  	print("\tUma curiosidade: " + infos['fato'])

#6.12 Extensoes

