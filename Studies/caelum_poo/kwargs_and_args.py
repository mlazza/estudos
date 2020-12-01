'''
1.	 Crie	um	arquivo	com	uma	função	chamada		teste_args_kwargs()		que	 recebe	três	argumentos	e
imprime	cada	um	deles:
					def	teste_args_kwargs(arg1,	arg2,	arg3):
									print("arg1:	",	arg1)
									print("arg2:	",	arg2)
									print("arg3:	",	arg3)
2.	 Agora	vamos	chamar	a	função	utilizando	o	*args:
					args	=	('um',	2,	3)
					teste_args_kwargs(*args)
Que	gera	a	saída:
					arg1:	um
					arg2:	2
					arg3:	3

3.	 Teste	a	mesma	função	usando	o	**kwargs.	Para	isso,	crie	um	dicionário	com	três	argumentos:
					kwargs	=	{'arg3':	3,	'arg2':	'dois',	'arg1':	'um'}
					teste_args_kwargs(**kwargs)
Que	deve	gerar	a	saída:
					arg1:	um
					arg2:	dois
					arg3:	3

4.	 (Opcional)	Tente	chamar	a	mesma	função,	mas	adicionando	um	quarto	argumento	na	variável	args	e
kwargs	dos	exercícios	anteriores.	O	que	acontece	se	a	função	recebe	mais	do	que	3	argumentos?

5.	 De	que	maneira	você	resolveria	o	problema	do	exercício	anterior?
Discuta	com	o	instrutor	e	seus	colegas	quando	usar	*args	e	**kwargs.
'''

def teste_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

def teste_args(*args):
    for arg in args:
        print('- ', arg)

args = ('um', 2, 3)
teste_args(*args)

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4': 4}
teste_kwargs(**kwargs)

