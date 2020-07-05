#5.6 Estágios da vida
#if-elif-else p var age
#<2a = bebe; 2/<4=crianca; 4-<13=garoto;13-<20=adolescente;20-<65=adulto;65+=idoso

print("Teste da idade:")
chave = True

while chave==True:
    age = int(input("Coloque a sua idade: ('-1' para sair)\n"))

    if age == -1:
        break
    if age < 2:
    	print("Bebê")
    elif age>=2 and age<4:
        print("Criança")
    elif age>=4 and age<13:
        print("Garoto")
    elif age>=13 and age<20:
        print("Adolescente")
    elif age>=20 and age<65:
        print("Adulto")
    elif age >= 65:
        print("Idoso")
    else:
        print("Digite um número válido!")
