"""1.Crie uma classe que modele o objeto "carro".
Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.
2. Crie uma instância da classe carro.
3. Faça o carro "andar" utilizando os métodos da sua classe.
4. Faça o carro "parar" utilizando os métodos da sua classe."""


class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 20
        self.velocidade_min = 0
        self.velocidade_max = 200

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelera(self, qtd):
        if not self.ligado:
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelera(self, qtd):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

    def __str__(self) -> str:
        return f"Carro ligado:{self.ligado},cor:{self.cor},modelo:{self.modelo}."


# Instâncias da classe Carro
meu_carro = Carro("preto", "gol")

meu_carro.ligar()
meu_carro.acelera(50)
print("A velocidade do carro nesse momento é {}".format(meu_carro.velocidade))
meu_carro.desacelera(20)
# meu_carro.desligar()

print("O carro está ligado?{}".format(meu_carro.ligado))
print(meu_carro)
print(meu_carro.acelera)
