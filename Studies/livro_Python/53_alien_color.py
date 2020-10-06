#5.3 Cores de alienígenas - Suponha que um alienígena acabou de ser atingido em um jogo. 
# Criar uma var 'alien color' e atribuir uma cor green, yellow ou red.
# Instrucao if par testa se a cor do alienigena é verde. Se for, mostrar msg informando q o jogador ganhou 5 pts
# Uma versao que o if falha mas nao manda nenhuma msg

#alien_color = 'green'
alien_color = 'red'

if alien_color == 'green':
	print("Parabéns player, você ganhou 5 pontos!")
elif alien_color == 'yellow':
	print("Você ganhou 10 pontos!")
elif alien_color == 'red':
	print("Você ganhou 15 pontos")
else:
	print("Cor inválida!")