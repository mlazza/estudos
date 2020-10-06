#5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma série de instruções if independentes que verifiquem se determinadas frutas estão em sua lista. • Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits. • Escreva cinco instruções if. Cada instrução deve verificar se uma determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por exemplo, Você realmente gosta de bananas!

frutas = ['maca', 'banana', 'conde', 'pessego']

print('maca' in frutas)

def verifica(fruta):
  if fruta in frutas:
    print("está na lista")
  else:
    print("nao está na lista")


verifica('acai')
verifica('banana')