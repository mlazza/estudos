# 9.4 Pessoas atendidas: comece com o programa em 9.1, acrescente um atributo chamado number_served
# cujo valor default é 0. Crie uma instancia chamada restaurant a partir dessa classe. Apresente o numero de
# clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente.

# Adicione um metodo chamado set_number_served() que permita definir o numero de clientes atendidos
# Chame esse metodo com um novo numero e mostre o valor novamente. 

# Acrescente um novo metodo chamado increment_number_served() que permita incrementar o numero de clientes servidos.
# Chame esse metodo com qualquer numero que voce quiser e que represente quantos clientes foram atendidos, por exemplo,
# em um dia de funcionamento.

#9.4

class Restaurant():
    def __init__(self, name, cuisin_type):
        self.name = name
        self.cuisin_type = cuisin_type
        self.number_served = 0
    
    def describe_rest(self):
        print('O nome do restaurante: ', self.name)
        print('O tipo de cozinha: ', self.cuisin_type)
        print('Numero de clientes atendidos: ', str(self.number_served))
    
    def open_rest(self):
        print('O restaurante está aberto!')

    def set_number_served(self, num):
        self.number_served = num
    
    def increment_number_served(self, num):
        self.number_served += num

'''
restaurant = Restaurant('Tony Stark', 'Italian Food')
restaurant.describe_rest()
restaurant.open_rest()

#setting a new number
restaurant.set_number_served(10)
restaurant.describe_rest()

#incrementing a number
restaurant.increment_number_served(22)
restaurant.describe_rest()
'''

# 9.5 Tentativas de login: Acrescente um atributo chamado login_attempts a sua classe User do exercicio 9.3. Escreva um metodo
# chamado increment_login_attempts que incremente o valor de login_attempts em 1. Escreva outro metodo chamado reset_login_attempts
# que reinicie o valor de login_attempts com 0.
# Crie uma instancia da classe User e chame increment_login_attempts() varias vezes. Exiba o valor de login_attempts para garantir que ele
# foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para garantir que seu valor
# foi reiniciado com 0.

# 9.3

class User():
    def __init__(self, first_name, last_name, email, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('Nome: ', self.first_name + ' ' + self.last_name)
        print('E-mail: ', self.email)
        print('Age: ', str(self.age))
        print('Sex: ', self.sex)
        print('Tentativas de Login: ', self.login_attempts)

    def greet_user(self):
        print('Olá, ', self.first_name + '. Tenha um bom dia!')
'''
usuario = User('Fabio', 'Donald', 'fbdonald@uol.com', 32, 'M')
usuario.describe_user()
usuario.greet_user()

for i in range(9):
    usuario.increment_login_attempts()

usuario.describe_user()
usuario.reset_login_attempts()
usuario.describe_user()
"""
'''
# 9.6 Sorveteria: Uma sorveteria é um tipo especifico de restaurante. Escreva uma classe chamada IceCreamStand que herde da classe
# Restaurant escrita no ex. 9.1 ou 9.4. Qualquer versao da classe funcionara, basta escolher aquela de que voce mais gosta. Adicione um 
# atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva um metodo para mostrar esses sabores. Crie uma instancia
# de IceCreamStand e chame esse método.

class IceCreamStand(Restaurant):
    '''Representa uma sorveteria'''
    def __init__(self, name, cuisin_type):
        super().__init__(name, cuisin_type)
        self.flavors = ['creme', 'chocolate', 'morango']


    def show_flavors(self):
        print('Os sabores são: ', self.flavors)
'''
sorveteria = IceCreamStand('Zé Gelato', 'Sorvetes')
sorveteria.describe_rest()
sorveteria.show_flavors()
'''

# 9.7 Admin: Um administrador é um tipo especial de usuário. Escreva uma classe chamada Admin que herde da classe User escrita no exerc.
# 9.3, ou ex. 9.5. Adicione um atributo privileges qye armazene uma lista de strings como 'can add post', 'can delete post', 'can ban user', 
# e assim por diante. Escreva um metodo chamado show_privileges() que liste o conjunto de privilegios de um administrador. Crie uma instancia
# de Admin e chame seu metodo. e 9.8 transferindo metodo show privileges para uma classe

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Os privilegios são: ', self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, email, age, sex):
        super().__init__(first_name, last_name, email, age, sex)
        self.privileges = Privileges()


# administrator = Admin('Jorge', 'Amado', 'jamado@bol.com.br', 55, 'M')
# administrator.privileges.show_privileges()

# 9.9 - Upgrade de bateria: use a ultima versao de electric_car.py. Acrescente um metodo chamado upgrade_battery() na classe
# Battery(). Esse metodo deve verificar a capacidade da bateria e defini-la com 85 se o valor for diferente. Crie um carro eletrico
# com uma capacidade de bateria default, chame get_range() uma vez, e em seguida, chame get_range() uma segunda vez apos fazer um upgrade
# da bateria. Voce devera ver um aumento na distancia que o carro é capaz de percorrer.

import electric_car as ec

carro1 = ec.ElectricCar('VW', 'Golf', 1998)
carro1.battery.get_range()
carro1.battery.upgrade_battery()
carro1.battery.get_range()