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

    def extrato(self):
        print("O saldo é de {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
