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

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Os privilegios são: ', self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, email, age, sex):
        super().__init__(first_name, last_name, email, age, sex)
        self.privileges = Privileges()