#7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
#os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
#finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
#mostre uma mensagem para cada pedido, por exemplo, Preparei seu
#sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
#para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
#prontos, mostre uma mensagem que liste cada sanduíche preparado.


sandwich_orders = ['queijo', 'x-salad', 'misto', 'bauru']
finished_sandwiches = []

print(sandwich_orders)

while sandwich_orders:
    
    print("\t" + sandwich_orders[0] + " preparado!")
    
    recorte = sandwich_orders.pop(0)
    finished_sandwiches.append(recorte)

print("\nSanduiches que saíram: ")
print(finished_sandwiches)
print(sandwich_orders)
    

#7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
#que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
#Acrescente um código próximo ao início de seu programa para exibir uma
#mensagem informando que a lanchonete está sem pastrami e, então, use um
#laço while para remover todas as ocorrências de 'pastrami' e
#sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
#finished_sandwiches.

print("\nPROGRAMA II")

sandwich_orders = ['queijo', 'pastrami', 'x-salad', 'misto', 'pastrami', 
                   'bauru', 'pastrami']
finished_sandwiches = []

print(sandwich_orders)
print("Estamos sem pastrami")

while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    
    print("\t" + sandwich_orders[0] + " preparado!")
    
    recorte = sandwich_orders.pop(0)
    finished_sandwiches.append(recorte)

print("\nSanduiches que saíram: ")
print(finished_sandwiches)
print(sandwich_orders)



#7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
#férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
#pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
#código que apresente os resultados da enquete.

print("PROGRAMA III - PERGUNTA E RESPOSTA")
respostas = {}

ativo = True

while ativo:
    nome = input("\nQual é o seu nome? ")
    resposta = input("\nQual é o seu sonho de férias? ")
    respostas[nome] = resposta

    repete = input("\nTem mais alguém para responder? (s / n) ")
    if repete == 'n':
        ativo = False

print("\nResultados: ")
for nome, resposta in respostas.items():
    print(nome + " gostaria de " + resposta + ".")