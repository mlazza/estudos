#Como comparar objetos no Python?

"""
Conhecendo a rich comparison
No Python temos como implementar algo similar ao equals(), mas ainda mais poderoso - a comparação rica, ou, como é tecnicamente conhecida, rich comparison . Com ela, podemos definir os seguintes métodos de comparação em uma classe:

__eq__(), chamado pelo operador ==
__ne__(), chamado pelo operador !=
__gt__(), chamado pelo operador >
__lt__(), chamado pelo operador <
__ge__(), chamado pelo operador >=
__le__(), chamado pelo operador <=
"""


class Filme():
	def __init__(self, titulo, diretor):
		self.titulo = titulo
		self.diretor = diretor

	def __eq__(self, outro_filme):
		return self.titulo == outro_filme.titulo

	def __str__(self):
		return self.titulo + ' - ' + self.diretor

	@property 
	def pega_todos_os_filmes(self):
		## implementação da função / faltou algo aqui....
		return self.titulo + self.diretor

	def tenho_o_filme(filme_procurado):
		meus_filmes = pega_todos_os_filmes()
		for filme in meus_filmes:
			if filme_procurado == filme:
				return True
		return False


goonies = Filme("Os Goonies", "John Adams")
titanic = Filme("Titanic", "Stevi Macdowell")


meus_filmes = pega_todos_os_filmes()

for filme in meus_filmes:
	print(filme)

filme_procurado = Filme("A Teoria de Tudo", "James Marsh")

if tenho_o_filme(filme_procurado):
    print("Tenho o filme!")
else:
    print("Não tenho :(")  