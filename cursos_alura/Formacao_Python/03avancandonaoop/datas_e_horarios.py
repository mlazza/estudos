#lidando com datas e horarios - post
#modulo datetime

from datetime import date

data_atual = date.today()
print(data_atual)

#podemos resolver o problema do formato da data com uma simples formatação de string:
data_em_texto = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"

#data_em_texto = f"0{data_atual.day}/0{data_atual.month}/{data_atual.year}" Colocar o zero antes não soluciona todos os casos.

print(data_em_texto)

#Formatando datas em strings usando o método strftime()

outro_met_data = data_atual.strftime('%d/%m/%Y')
print(outro_met_data)

#Uma das vantagens da classe datetime é que ela consegue cuidar da data e do horário ao mesmo tempo.
#A única diferença em nosso uso é que, em vez do método today(), usaremos o método now():

from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

print(data_e_hora_em_texto)

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

#Se tivéssemos uma string de data e quiséssemos transformar em datetime, o que faríamos?
#Novamente, um simples método resolve tudo, dessa vez o strptime(), da própria classe datetime:

from datetime import datetime

data_e_hora_em_texto = "01/03/2018 12:30"
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')

print(data_e_hora.strftime('%d/%m/%Y %H:%M'))

#timezone

from datetime import datetime, timezone, timedelta

#O problema é que o construtor timedelta recebe vários outros argumentos além da hora, nessa ordem:
#days (dias)#seconds (segundos)#microseconds (microsegundos)#milliseconds (milisegundos)#minutes (minutos)
#hours (horas)#weeks (semanas)

data_e_hora_atuais = datetime.now()
#fuso_horario = timezone(-3)
#print(fuso_horario)

diferenca = timedelta(hours=-3)
print(diferenca)

#Vamos, agora, criar um objeto timezone correspondente ao UTC-3, indicando essa diferença do UTC como parâmetro do construtor:

fuso_horario = timezone(diferenca)
print(fuso_horario)

#Finalmente, podemos converter o tempo da máquina para o de São Paulo, usando o método astimezone():

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

#A comunidade Python, frente a essa necessidade, criou diversas bibliotecas para facilitar a manipulação de timezones, 
#como a pytz. Para instalar a pytz, você pode usar o pip pelo terminal:
#>>pip install pytz
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

#A CONCLUIR INSTALANDO PIP AND PYTZ.... https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python