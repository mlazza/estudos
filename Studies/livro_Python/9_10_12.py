# 9.10 Usando sua classe Restaurant mais recente, armazene-a em um modulo. Crie um arquivo separado que importe Restaurant.
# Crie uma instancia de Restaurant e chame um de seus metodos para mostrar que a instrucao import funciona de forma apropriada.

import restaurant as rs

podrao = rs.Restaurant('Podrao Lanchonete', 'Lanches')
podrao.describe_rest()

# 9.11 - Importando Admin: comece com seu programa do exercicio 9.8. Armazene as classes User, Privileges e Admin em um modulo.
# Crie um arquivo separado e uma instancia de Admin e chame show_privileges() para mostra que tudo está funcionando de forma apropriada.

import modulo_user as mu

usuario = mu.Admin('Debora', 'Cristina', 'dc@yahoo.com', 37, 'F')
usuario.privileges.show_privileges()

# 9.12 OK