#5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista com um laço e mostre uma saudação para cada usuário: • Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um relatório de status? 127 • Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por fazer login novamente.

lista = ['tony', 'admin', 'tiago', 'rafael', 'rodrigo']

for nome in lista:
  if(nome == 'admin'):
    print("Olá admin. Gostaria de ver o relatório diário?")
  else:
    print("Olá " + nome + ", seja bem-vindo ao sistema!")


# 5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a lista de usuários não esteja vazia. • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários! • Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.

lista2 = []
if lista2:
  print("Lista não está vazia!")
else:
  print("Lista está vazia!")

#5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa que simule o modo como os sites garantem que todos tenham um nome de usuário único. • Crie uma lista chamada current_users com cinco ou mais nomes de usuários. • Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois dos novos usuários também estejam na lista current_users. • Percorra a lista new_users com um laço para ver se cada novo nome de usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado, apresente uma mensagem dizendo que o nome do usuário está disponível. • Certifique-se de que sua comparação não levará em conta as diferenças entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser aceito.

usuarios_current = ['jorge', 'afonso', 'gilmar', 'tony', 'eliz']
new_users = ['eliz', 'cesar', 'gilmar', 'daniel', 'celso']

user = input("Digite o nome de usuário: ")
user = user.lower()
print(user)
new_users.append(user)

if user in usuarios_current:
    print(user + " já existe no cadastro. Favor utilizar outro!")
else:
    print(user + " não existe no cadastro")
