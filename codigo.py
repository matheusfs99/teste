class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor} realizado. Novo saldo: R$ {self.saldo}')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado. Novo saldo: R$ {self.saldo}')
        else:
            print('Saldo insuficiente para realizar o saque.')
    
    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f'Transferência de R$ {valor} realizada para a conta de {conta_destino.titular}. Novo saldo: R$ {self.saldo}')
        else:
            print('Saldo insuficiente para realizar a transferência.')
    
    def consultar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo}')