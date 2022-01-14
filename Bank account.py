class Conta():
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def saca(self, valor):
        if valor > self.saldo:
            print(f'Impossível sacar valor, pois saldo não permite.')
        else:
            self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f'O saldo da sua conta é: {self.saldo}')



conta1 = Conta("Guilherme", "123", 1000.0)

conta1.saca(1001)
conta1.deposita(1)
conta1.extrato()