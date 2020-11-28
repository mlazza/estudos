
class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def	deposita(self,	valor):
        self._saldo += valor


    def __str__(self):
        return "Dados da conta: \nNumero: {} \nSaldo: {} \nLimite: {}".format(self._numero, self._titular, self._saldo, self._limite)


class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite=0):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
    
    def deposita(self, valor):
        self._saldo += valor - 0.1


class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo, limite=0):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    
    c = Conta('123-4', 'Joao Narguile', 1000)
    cc = ContaCorrente('123-5', 'Jair Tonhao', 1000)
    cp = ContaPoupanca('123-6', 'Maria Antonieta', 1000)

    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c._saldo)
    print(cc._saldo)
    print(cp._saldo)

    print(cp)