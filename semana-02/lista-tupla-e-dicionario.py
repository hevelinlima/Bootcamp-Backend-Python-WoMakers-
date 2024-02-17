"""1.Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno imprima o número de alunos com média maior ou igual a 7.0.

#Código inicial para um aluno

nota=(input('Informe as 4 notas bimetrais de um aluno, separadas por vírgula(Ex: 10,7,9,8):'))

notas=nota.split(',')

if len(notas) != 4:
  print('Por favor, insira QUATRO notas.')
else:
  nota1=float(notas[0])
  nota2=float(notas[1])
  nota3=float(notas[2])
  nota4=float(notas[3])

  med=(nota1+nota2+nota3+nota4)/4
  print(f'A média do aluno é {med}')

#Código da questão para os 10 alunos

medias=[]

quant_alunos=10
  
for i in range(quant_alunos):
  print(f'Aluno{i+1}:')
  notas_alunos=[]

  nota=(input('Informe as 4 notas bimetrais de um aluno, separadas por vírgula(Ex: 10,7,9,8):'))

  notas=nota.split(',')

  if len(notas) != 4:
    print('Por favor, insira QUATRO notas.')
  else:
    nota1=float(notas[0])
    nota2=float(notas[1])
    nota3=float(notas[2])
    nota4=float(notas[3])
  
    notas_alunos.extend([nota1, nota2, nota3, nota4])

    med=sum(notas_alunos)/len(notas_alunos)
    medias.append(med)

alunos_aprovados = sum(1 for media in medias if media >= 7.0)
print(f'Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}')"""

"""2. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica:lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome=input("Digite o seu nome:")
nome_maiusc=nome.upper()
inverso_nome=nome_maiusc[::-1]

print(f'O seu nome de trás para frente é: {inverso_nome}')"""

"""3. Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim, imprima True. Caso contrário, imprima Falso.

def all_keys_have_values(dicionario):
    return all(value is not None for value in dicionario.values())

customer = {
    'nome': 'Rafael',
    'idade': None,
    'cidade': "Rio de janeiro"
}

resultado=all_keys_have_values(customer)

print(resultado)"""


"""4.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice " e 5 como "Assassino".Caso contrário, ele será classificado como "Inocente".."""

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " Responda sim ou não: ").lower()
    if resposta == "sim":
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Suspeito")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
