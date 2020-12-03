import datetime


class Conta:

    def __init__(self, numero, cliente, saldo, limite=0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print('saldo nao pode ser negativo')
        else:
            self._saldo = saldo

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self._numero, self._saldo))
        self.historico._transacoes.append('tirou extrato - saldo de {}'.format(self._saldo))

    def deposita(self, valor):
        self._saldo += valor
        self.historico._transacoes.append('depósito de {}'.format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico._transacoes.append('saque de {}'.format(valor))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico._transacoes.append('transferencia de {} para conta {}'.format(valor, destino._numero))
            return True


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf


class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    def imprime(self):
        print('Data de abertura: {}'.format(self._data_abertura))
        print('transações: ')
        for t in self._transacoes:
            print('-', t)


cliente1 = Cliente('Marlon', 'Lazzarotti', '212121212-00')
cliente2 = Cliente('Rochelle', 'Lazzarotti', '000121212-00')

conta1 = Conta('123-1', cliente1, 1000)
conta2 = Conta('124-1', cliente2, 1000)
print('1')
conta1.deposita(100)
conta1.saca(50)
print('2')
conta1.transfere_para(conta2, 200)
conta1.extrato()

conta1.historico.imprime()
conta2.historico.imprime()

#print(vars(conta1)) - listando os atributos de uma conta