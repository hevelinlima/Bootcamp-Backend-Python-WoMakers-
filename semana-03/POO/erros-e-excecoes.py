"""O programa abaixo deve calcular a média dos valores digitados pelo usuário. No entanto, ele não está funcionando bem. Você pode consertá-lo?

#Código com erro

def calcular_media(valores):
  tamanho=1
  soma=0.0
  for i, valor in enumerate(valores):
    soma+= valor
    i+=1
  media=soma/tamanho

continuar=True
valores=[]
while continuar:
  valor=input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
  if valor.lower()=='ok':
    continuar=False

media=calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores,media))"""

# Código consertado

# a soma é definida pela soma dos números recebidos na lista valores e então é dividido pela variável tamanho que foi definida como o tamanho/comprimento da lista


def calcular_media(valores):
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho
    return media


continuar = True
valores = []

while continuar:
    valor = input(
        'Digite um número para entrar na sua média ou "ok" para calcular o valor:'
    )
    if valor.lower() == "ok":
        continuar = False

    # valor_num converte o texto recebido no input para int e guarda o resultado em na lista de valores

    else:
        valor_num = int(valor)
        valores.append(valor_num)

media = calcular_media(valores)
print("A média calculada para os valores {} foi de {}".format(valores, media))
