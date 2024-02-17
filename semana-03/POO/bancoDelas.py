"""O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres. Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
- Cada conta corrente pode ter um ou mais clientes como titular.
- O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
- A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
- Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente.Quando ela fizer um depósito, aumentaremos o saldo.
- Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até renda_mensal.
- Clientes homens por enquanto não têm direito a cheque especial.

Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata"."""

from abc import ABC, abstractmethod


class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if type(novo_nome) != str:
            raise TypeError("Esta variável deve ser string!")
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) != str:
            raise TypeError("Esta variável deve ser string!")
        self._telefone = novo_telefone

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @abstractmethod
    def cheque_especial(self):
        pass


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def cheque_especial(self):
        return True


class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def cheque_especial(self):
        return False


class ContaCorrente:
    def __init__(self):
        self.__titulares = []
        self.__saldo = 0
        self.__lista_operacoes = []

    def adc_titular(self, titular):
        self.__titulares.append(titular)

    def listar_titulares(self):
        for titular in self.__titulares:
            print(titular.nome)

    def deposito(self, valor):
        self.__saldo += valor
        self.__lista_operacoes.append(valor)
        print(f"Você depositou R${valor}reais.")

    def saque(self, valor):
        if self.__saldo - valor >= 0 or any(
            titular.cheque_especial() for titular in self.__titulares
        ):
            self.__saldo -= valor
            self.__lista_operacoes.append(-valor)
            print(f"Você sacou R${valor}reais.")
        else:
            print("Seu saldo é insuficiente")

    @property
    def saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Cliente: {[titular._nome for titular in self.__titulares]}")
        print(f"Saldo: R${self.__saldo:.2f}")
        print("Operações:")
        for operacoes in self.__lista_operacoes:
            print(operacoes)


# Criando clientes
cliente_mulher = ClienteMulher("Hemilly", "123-456", 5000)
cliente_homem = ClienteHomem("Sávio", "789-123", 10000)

# Criando contas correntes
conta_maria = ContaCorrente()
conta_joao = ContaCorrente()

# Adicionando titulares às contas
conta_maria.adc_titular(cliente_mulher)
conta_joao.adc_titular(cliente_homem)

# Realizando operações
conta_maria.deposito(1000)
conta_maria.saque(2000)
conta_maria.extrato()

conta_joao.deposito(800)
conta_joao.saque(1000)
conta_joao.extrato()
