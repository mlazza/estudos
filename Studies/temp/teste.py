
import re
import numpy as np

# pylint: disable=no-member
# pylint: disable=too-many-locals
#p1 - preto e branco - pode ou nao vir separado por espaco
#p2 - tons de cinza - vem separado por espaco ou tabulacao ou separador
#p3 - colorido - idem p2, e sao 3 numeros = RGB

#cabecalho do arquivo:
#"Px"
#Comentario (opt) começam com '#' e final com quebra de linha, programa deve ignorar estes comments,
# comecando pela linha seguinte
# Larg x Alt (matriz)
# max_value (opt)

# OBS: o arquivo pode ter diversos espaços em branco e quebras de linha!

#calculos

#a) comparar o valor dos pixels com a metade de max_value
#exemplo: uma imagem p2 (tons de cinza) tem max_value = 100, sendo que todos os pixels presentes em seu corpo
# tem valor < 70, neste caso CONTAR pixels > 50 (metade do max_value)
#
#b) no caso de p3 (coloridas), use a MEDIA entre estes 3 valores para fazer a comparacao com MAX_VALUE

#FUNCOES
def limpeza(linhas):
    lista_limpa = []
    for linha in linhas:
       # print(linha)
        if 'p1' in linha.strip().lower():
            print('aqui tem arquivo p1')
            return 'p1'
        elif 'p2' in linha.strip().lower():
            print('aqui tem arquivo p2')
            return 'p2'
        elif 'p3' in linha.strip().lower():
            print('aqui tem arquivo p3')
            return 'p3'
        if '#' in linha.strip():
           print(linha)
        else:
           lista_limpa.append(linha)
        if linha.isspace():
            del(linha)
        else:
           lista_limpa.append(linha)
    return lista_limpa

def comentario(linhas):
    '''ignoring row with comment'''
    no_comment = []
    for linha in linhas:
       if '#' in linha.strip():
           print(linha)
       else:
           no_comment.append(linha)
    return no_comment

def removing_spaces_lines(linhas):
    no_spaces = []
    for linha in linhas:
        if linha.isspace():
            del(linha)
        else:
           no_spaces.append(linha)
    return no_spaces


def acertando_matriz():
    pass



def contagem():
    pass


#ENTRADA - arquivo p1, p2 ou p3 em formato PNM ASCII do NetPBM

arquivo = open('circle.pnm', 'r')

linhas = []

for linha in arquivo:
    linhas.append(linha)

#print()
'''
tipo_sem_p = qual_o_tipo(linhas)
sem_comentario = comentario(tipo_sem_p)
sem_linhas_vazias = removing_spaces_lines(sem_comentario)
'''
lista = limpeza(linhas)
print(lista)


#p1(linhas)







#SAIDA

#contagem - numero inteiro

