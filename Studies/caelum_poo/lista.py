'''
Vamos tentar	resolver	alguns	desafios.	Dada	a	lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
faça	um	programa	que:
a)	imprima	o	maior	elemento
b)	imprima	o	menor	elemento
c)	imprima	os	números	pares
d)	imprima	o	número	de	ocorrências	do	primeiro	elemento	da	lista
e)	imprima	a	média	dos	elementos
f)	imprima	a	soma	dos	elementos	de	valor	negativo
'''
import statistics as st

lista = [12, -2, 3, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

a = max(lista)
print('Maior valor: ', a)

b = min(lista)
print('Menor valor: ', b)

c = []
for item in lista:
    if item % 2 == 0:
        c.append(item)
print(c)

d = lista.count(lista[0])
print(d)

e = st.mean(lista)
print(e)

f = 0
for item in lista:
    if item < 0:
        f += item
print(f)

