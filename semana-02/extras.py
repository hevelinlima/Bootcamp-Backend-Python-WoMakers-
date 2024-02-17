"""1.Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo: 
Dólar Americano:R$4,91 
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suiço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21

dinheiro=float(input('Quanto dinheiro você tem na carteira neste momento?'))

dolar_americano=dinheiro/4.91
print(f'Você tem {dolar_americano:.2f} dolares americanos.')

peso_argentino=dinheiro/0.02
print(f'Você tem {peso_argentino:.2f} pesos argentinos.')

dolar_australiano=dinheiro/3.18
print(f'Você tem {dolar_australiano:.2f} dolares australianos.')

dolar_canadense=dinheiro/3.64
print(f'Você tem {dolar_canadense:.2f} dolares canadenses.')

franco_suico=dinheiro/0.42
print(f'Você tem {franco_suico:.2f} francos suíços.')

euro=dinheiro/5.36
print(f'Você tem {euro:.2f} euros.')

libra=dinheiro/6.21
print(f'Você tem {libra:.2f} libras.')"""

"""2. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço apagar, sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado.

km_percorridos=int(input('Quantos km você percorreu com o carro alugado?'))
dias_aluguel=int(input('Por quantos dias você alugou o carro?'))
valor_por_dia=80
valor_por_km=0.2

valor_a_pagar=(dias_aluguel*valor_por_dia)+(km_percorridos*valor_por_km)
print(f'O valor a ser pago pelo carro alugado é R${valor_a_pagar:.2f} reais.')"""

"""3. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Se o salário for até R$1000,00 o funcionário terá 20% de aumento. Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento.Acima de R$2801,00 o funcionário terá 5% de aumento

salario_atual=int(input('Qual o seu salário atualmente?'))
if salario_atual<=1000:
  novo_salario=salario_atual+(salario_atual*0.2)
  print(f'Seu novo salário será R${novo_salario} reais.')
elif 1001<=salario_atual<=2800:
  novo_salario=salario_atual+(salario_atual*0.1)
  print(f'Seu novo salário será R${novo_salario} reais.')
elif salario_atual>=2800:
  novo_salario=salario_atual+(salario_atual*0.05)
  print(f'Seu novo salário será R${novo_salario} reais.')
else:
  print('ERRO')."""

"""4. Crie um programa que tenha a função leiaInt(),que vai funcionar de forma semelhante à função input() do Python,só que fazendo a validação para aceitar apenas um valor númerico. Ex: n= leiaInt('Digite um n')"""


def leiaInt(message):
    while True:
        try:
            numero = int(input(message))
            if numero == 5:
                return numero
            else:
                print("Número errado, desculpe.Digite o número 5.")
        except ValueError:
            print("Valor inválido, desculpe. Tente novamente.")


n_cinco = leiaInt("Digite o número 5: ")
print(f"Você digitou o número: {n_cinco}")
