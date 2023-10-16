# ler anual
sal = int(input("insira o salario anual: "))

# avaliar se o salario e igual ou menor
if sal == 15000:
    imposto=sal*0.2
    print("paga a taxa de 20 porcento", imposto)
if sal >15000 and sal<=20000:
    imposto = sal*0.3
    print("paga a taxa de 30 por cento",imposto)
if sal == 20000 and sal <= 25000:
    imposto = sal*0.35
    print("Paga a taxa de 35", imposto)
if sal > 25000:
    imposto = sal*0.6
    print("a taxa e de 40",imposto)