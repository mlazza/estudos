import jogo_adivinha as adv
import forca as fc

print('*****************************************')
print('*****************************************')
print('*************MENU DE JOGOS***************')
print('*****************************************')
print('*****************************************')

print('1 - Adivinhacao')
print('2 - Forca')

escolha = int(input('Qual jogo quer jogar? Digite o número: '))

if escolha == 1:
    adv.jogar()
elif escolha == 2:
    fc.jogar()