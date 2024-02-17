"""1.Faça um programa, com uma função que necessite de três argumentos,e que forneça a soma desses três argumentos.

def soma(num1,num2,num3):
  calc=num1+num2+num3
  print(f'A soma dos números dados é: {calc}')

num1=int(input('Digite um número:'))
num2=int(input('Digite um número:'))
num3=int(input('Digite um número:'))

soma(num1,num2,num3)"""

"""2."Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado. Porexemplo:127->721.

def inverso(numero):
  if numero<0:
    return int(str((abs(numero)))[::-1])
  else:
    return int(str((numero))[::-1])

numero=int(input('Digite um numéro:'))
inverso_numero=inverso(numero)

print(f"O reverso de {numero} é {inverso_numero}")"""


"""3.Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção,crie uma função. Crie uma terceira,que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta."""

resposta = input("Você deseja realizar uma conversão de temperatura?")
if resposta == "sim":

    def farenheit_celsius(temp_fahrenheit):
        temp_celsius = (temp_farenheit - 32) * 5 / 9
        return temp_celsius

    def celsius_farenheit(temp_celsius):
        temp_farenheit = (temp_celsius * 9 / 5) + 32
        return temp_farenheit

    def menu():
        print("Escolha uma das conversões:")
        print("1. Fahrenheit para Celsius")
        print("2. Celsius para Fahrenheit")
        print("0. Fechar menu.")

    while True:
        menu()
        conversao = input("Digite a opção desejada:")

        if conversao == "1":
            temp_farenheit = float(input("Digite a temperatura em Fahrenheit: "))
            temp_celsius = farenheit_celsius(temp_farenheit)
            print(f"{temp_farenheit}°F é igual a {temp_celsius:.2f}°C\n")

        elif conversao == "2":
            temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
            temp_farenheit = celsius_farenheit(temp_celsius)
            print(f"{temp_celsius}°C é igual a {temp_farenheit:.2f}°F\n")

        elif conversao == "0":
            break

        else:
            print("Indisponível. Digite 1 ou 2.")

elif resposta == "não":
    print("Ok :)")

else:
    print("Não entendi :/")
