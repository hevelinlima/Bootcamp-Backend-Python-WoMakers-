""" 1.Faça um Programa que peça um número e então mostre a mensagem: -> O número informado foi [número].

numero=int(input('Digite um número qualquer:'))
print(f'O número informado foi: {numero}')"""

"""2.Faça um Programa que peça dois números e imprima a soma.

numero1=int(input('Digite um número:'))
numero2=int(input('Digite outro número:'))
soma = numero1 + numero2
print(f'A soma dos dois números dados é: {soma}')"""

"""3.Faça um Programa que peça a temperatura em graus Celsius,transforme e mostre em graus Fahrenheit.

temp_celsius= float(input('Indique uma temperatura em graus Celsius:'))
temp_farenheit=(temp_celsius*9/5)+32
print(f'A temperatura que você indicou é {temp_farenheit} em Farenheit.')"""

"""4 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

salario_hora=int(input('Quanto você ganha por hora?'))
horas_trab_mes=int(input('Quantas horas você trabalha por mês?'))
salario_mes=salario_hora*horas_trab_mes
print(f'De acordo com as informações recebidas, o salário que você recebeu no referido mês foi {salario_mes} reais.')