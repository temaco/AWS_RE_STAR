# ler anual
sal = float(input("insira o salario anual"))
# avaliar se o salario e igual ou menor
if sal <= 15000:
    imposto = sal*0.2
    print("paga a taxa de 20 porcento", imposto)
else:
    imposto = sal*0.3
    print("paga a taxa de 30 por cento",imposto)