#criando uma classe Funcionario

# CLASSE FUNCIONARIO
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    # métodos
    def get_bonificacao(self):
        return self._salario * 0.1

# CLASSE GERENTE
class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

    # métodos

    def autentica(self, senha):
        if self._senha == senha:
            print('acesso permitido')
            return True
        else:
            print('acesso negado')
            return False

# CLASSE DE BONIFICACOES
class ControleBonificacoes:

    def __init__(self, tota_bon=0):
        self._total_bon = tota_bon
    
    def registra(self, obj):
        try:
            self._total_bon += obj.get_bonificacao()
        except AttributeError as e:
            print(e)
    @property
    def total_bonificacoes(self):
        return self._total_bon

# CLASSE DE CLIENTE
class Cliente:

    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha








# PROGRAMA PRINCIPAL
if __name__ == '__main__':

    #acessando os atributos dos objetos instanciados com vars():
    
    gerente = Gerente('Jose', '222222222-22', 5000, '1234', 0)
    #print(vars(gerente))

    funcionario = Funcionario('Joao', '111111111-11', 2000)
    #print(vars(funcionario))'''

    print('bonificacao funcionario: {}'.format(funcionario.get_bonificacao()))
    print('bonificacao gerente: {}'.format(gerente.get_bonificacao()))

    controle = ControleBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)

    print('total de bonificacoes concedidas: {}'.format(controle.total_bonificacoes))