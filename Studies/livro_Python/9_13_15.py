# 9.13 Reescrevendo o programa com OrderedDict: comece com o exercicio 6.4, em que usamos um dicionario padrao para representar um 
# glossario. Reescreva o programa usando a classe OrderedDict e certifique-se de que a ordem da saida coincida com a ordem em que os pares
# chave-valor foram adicionados ao dicionario

#6.4 Glossário
from collections import OrderedDict

glossario = OrderedDict()

glossario['dicionário'] = 'Uma lista de valores de correspondência dupla, com chave : valor'
glossario['tupla'] = 'Uma lista de valores imutáveis, que não podem sofrer alteração depois de criados'
glossario['laço'] = 'Um evento de repetição, podendo ser utilizado com os comandos for, while'
glossario['variável'] = 'Uma reserva de memória para um valor determinado'
glossario['lista'] = 'Um conjunto de valores que podem ser guardados dentro de uma variável'
glossario['dicionário21'] = 'Uma lista de valores de correspondência dupla, com chave : valor'
glossario['tupla22'] = 'Uma lista de valores imutáveis, que não podem sofrer alteração depois de criados'
glossario['laço23'] = 'Um evento de repetição, podendo ser utilizado com os comandos for, while'
glossario['variável24'] = 'Uma reserva de memória para um valor determinado'
glossario['lista25'] = 'Um conjunto de valores que podem ser guardados dentro de uma variável'
'''
for key, value in glossario.items():
	print("\n" + key.title())
	print("\t" + value)
'''
# 9.14 Dados: O modulo random contem funcoes que geram numeros aleatorios de varias maneiras. A funcao randint() devolve um inteiro
# no intervalo especificado por voce. O codigo a seguir devolve um numero entre 1 e 6. x = randint(1, 6). 
# Crie uma classe Die com um atributo chamado sides, cujo valor default é 6. Escreva um metodo chamado roll_die() que exiba um numero
# aleatorio entre 1 e o numero de lados do dado. Crie um dado de seis dados e lance-os dez vezes.
# Crie um dado de dez lados e outro de vinte lados. Lance cada dados dez vezes.

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, x):
        for i in range(x):
            print('Rolando o dado - ' + str(i) + ' lance:' + str(randint(1, self.sides)))
'''
dado1 = Die()
dado2 = Die(10)
dado3 = Die(20)

dado1.roll_die(10)
dado2.roll_die(10)
dado3.roll_die(10)
'''

# 9.15 Modulo Python da Semana: pymotx.com/ >> explorar a doc dos modulos collections e random.


