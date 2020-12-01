'''
1.	 Defina	uma	função	chamada	velocidade_media()	em	um	script	chamado		funcoes.py		 que	 recebe
dois	parâmetros:	a	distância	percorrida	(em	metros)	e	o	tempo	(em	segundos)	gasto.
					def	velocidade_media(distancia,	tempo):
									pass
2.	 Agora	vamos	inserir	as	instruções,	ou	seja,	o	que	a	 função	deve	 fazer.	Vamos	inserir	os	comandos
para	calcular	a	velocidade	média	e	guardar	o	resultado	em	uma	variável		velocidade	:
					def	velocidade_media(distancia,	tempo):
									velocidade	=	distancia/tempo
3.	 Vamos	fazer	a	função	imprimir	o	valor	da	velocidade	média	calculada:
					def	velocidade_media(distancia,	tempo):
									velocidade	=	distancia/tempo
									print(velocidade)
4.	 Teste	 o	 seu	 código	 chamando	 a	 função	 para	 os	 valores	 abaixo	 e	 compare	 os	 resultados	 com	 seus

colegas:
distância:	100,	tempo	=	20
distância:	150,	tempo	=	22
distância:	200,	tempo	=	30
distância:	50,	tempo	=	3
5.	 Modifique	a	função		velocidade_media()		de	modo	que	ela	retorne	o	resultado	calculado.
6.	 Defina	uma	função		soma()		que	recebe	dois	números	como	parâmetros	e	calcula	a	soma	entre	eles.
7.	 Defina	uma	função		subtracao()	que	recebe	dois	números	como	parâmetros	e	calcula	a	diferença
entre	eles.
8.	 Agora	 faça	 uma	 função	 	calculadora()		 que	 recebe	 dois	 números	 como	 parâmetros	 e	 retorna	 o
resultado	da	soma	e	da	subtração	entre	eles.
9.	 Modifique	a	função		calculadora()		do	exercício	anterior	e	faça	ela	retornar	também	o	resultado	da
multiplicação	e	divisão	dos	parâmetros.
10.	 Chame	a	função		calculadora()		com	alguns	valores.
11.	 (opcional)	 Defina	 uma	 função	 	divisao()		 que	 recebe	 dois	 números	 como	 parâmetros,	 calcula	 e
retorna	o	resultado	da	divisão	do	primeiro	pelo	segundo.	Modifique	a	função		velocidade_media()
utilizando	a	função		divisao()		para	calcular	a	velocidade.	Teste	o	seu	código	chamando	a	função
	velocidade_media()		com	o	valores	abaixo:	a.	distância:	100,	tempo	=	20	b.	distância:	-20,	tempo
=	10	c.	distância:	150,	tempo	=	0
'''

def vel_media(distancia, tempo):
    return divisao(distancia, tempo)

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    return a/b

def calculadora(a, b):
    return a+b, a-b, a*b, a/b

print(calculadora(2, 5))
print(vel_media(100, 20))