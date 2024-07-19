class ContaBancaria:
    def __init__(self, account_number, account_holder, saldo=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}')
        else:
            print('Valor de depósito inválido.')
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Valor de saque inválido.')
    
    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                conta_destino.saldo += valor
                print(f'Transferência de R$ {valor:.2f} realizada para a conta de {conta_destino.account_holder}. Novo saldo: R$ {self.saldo:.2f}')
            else:
                print('Saldo insuficiente para realizar a transferência.')
        else:
            print('Valor de transferência inválido.')
    
    def consultar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo:.2f}')