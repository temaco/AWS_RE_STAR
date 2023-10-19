#Faça um programa que vai pedindo números ao utilizador até que este introduza o número -1.
# O computador deve dizer a média dos números introduzidos (excluindo o -1
# Inicializa as variáveis
numero=0
soma = 0
contador = 0

while numero != -1:
    numero = int(input("Digite um número: "))

    if numero != -1:
        print()

    soma += numero
    contador += 1

# Calculo
if contador > 0:
    print(soma)
    print(contador)
    media = soma / contador-numero
    print("A média dos números introduzidos  é: ",media)

