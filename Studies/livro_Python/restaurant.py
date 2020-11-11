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
