"""1.Faça um programa que peça dois números e imprima o maior deles.

numero1= int(input('Digite um número qualquer:'))
numero2= int(input('Digite outro número:'))
if numero1>numero2:
  print(f'O número {numero1} é maior.')
elif numero2>numero1:
  print(f'O número {numero2} é maior.')
else:
  print(f'Os números informados são iguais')"""

"""2.Faça um programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "BomDia!", "BoaTarde!" ou "BoaNoite!" ou "ValorInválido!", conforme o caso.

turno=input('Em qual turno você estuda? Digite M para matutino, V para Vespertino ou N para Noturno.')
if turno=="M":
  print('Bom dia!')
elif turno=="V":
  print('Boa Tarde!')
elif turno=="N":
  print('Boa Noite!')
else:
  print('Valor inválido')"""

"""3.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

nota = int(input("Digite uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido")
    nota = int(input("Digite uma nota entre 0 e 10: "))

print(f"A nota inserida foi: {nota}")
