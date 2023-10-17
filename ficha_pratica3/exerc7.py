#Faça um programa que leia um número inteiro e imprima os 5 anteriores e os 5 seguintes.
numero = int(input("Digite um número inteiro: "))
anterior = numero - 5

# Imprime os cinco números anteriores
while anterior < numero:
    print(anterior)
    anterior += 1

# Imprime o próprio número
print(numero)

posterior = numero + 1

# Imprime os cinco números seguintes
while posterior < numero + 5:
    print(posterior)
    posterior = posterior + 1

