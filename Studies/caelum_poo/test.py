def	cria_conta(numero, titular, saldo, limite):
    conta ={"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def	deposita(conta,	valor):
    conta['saldo'] = conta['saldo']	+ valor


def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

conta1 = cria_conta('123-4', 'João', 120.0,	1000.0)
conta2 = cria_conta('123-5', 'José', 200.0,	1000.0)

saca(conta1, 30)
extrato(conta1)