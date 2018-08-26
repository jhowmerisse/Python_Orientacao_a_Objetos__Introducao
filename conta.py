class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor_saque):
        saldo_disponivel = self.__saldo + self.__limite
        return saldo_disponivel >= valor_saque

    def extrato(self):
        print("O saldo é de {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("saldo insuficiente")

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
