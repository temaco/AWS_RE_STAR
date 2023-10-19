#*******BLOCO1********************
#Para um determinado quarto:
# Custo: +200€/dia reservado
# Limpeza: -15€/dia reservado
#Descontos fiscais: -23% (lucro)

#*************BLOCO 2 *****************
#apresentar:
#• O valor ilíquido a receber pelas reservas totais. (Apenas custo)
#• Total do custo da limpeza.
#• Valor de descontos fiscais a entregar ao estado.
#• Valor líquido a receber pelo quarto. (Custo-Limpezas-Descontos Fiscais)
#----------------------------------------------------*******************************************

#Solicitar número do quarto

quarto = int((input("Qual é o número do quarto desejado ? ")))
#Solicitar o numero de dias que vai ficar reservado sobre o total de um ano /365
dias = int(input("Qual é o número de dias que o quarto esteve reservado? "))

# Declaracao de variaveis

custo_dia = 200
limpeza_dia = 15
impostos1 = 0.23


              # delcarar lucro sem despesas
print("Valor ilíquido: ", custo_dia * dias)

print("Custos de limpeza : ", dias * limpeza_dia)
        #impostos pagos ao Estado
print("Tem a pagar ao estado :", dias * custo_dia * impostos1)
        #valor liquido a receber pelo quarto
print("Valor líquido : ",(custo_dia * dias +(-limpeza_dia)) * 0.77 )

#alterar program de modo adicionar o stipos de quartos

impostos2=0.25
impostos3=0.28

I = 200
D = 250
T = 300
S = 350

limpezaI = 15
limpezaD = 20
limpezaT = 20
limpezaS = 30

     #lucro = dias * tipo_quarto
quarto = (input("Digite o tipo de carro: I - Individual,D - DuploT - Triplo-S - Suíte"))

servico_desejado = input(":")
       #Quarto seleccionado , custo +limpeza +desconto fiscal
servico_desejado =(input("Qual o serviço desejado? 1.Contabilidade   2.Quartos de vago ?"))
    #Serviços
if servico_desejado == "1":

        if quarto == "I":
            print("Quarto indivdual")
            valor_iliquido = 200 * dias
            custo_limpeza = 15 * dias


        if quarto =="D" :
            print("Quarto duplo")
            valor_iliquido = 250 * dias
            custo_limpeza = 20 * dias
        if quarto =="T" :
            print("Quarto triplo")
            valor_iliquido = 275 * dias
            custo_limpeza = 20 * dias
        if quarto =="S":
            print("Quarto suíte")
            valor_iliquido = 350 * dias
            custo_limpeza = 30 * dias
        print("Lucro ilíquido: ",valor_iliquido)
        print("Custos de limpeza: ",custo_limpeza)

          #Descontos fiscais
        if (valor_iliquido <= 20000) :
            impostos = valor_iliquido * impostos1
            print("Tem a pagar ao estado 23% do valor que arrecadas :€",impostos)

        if ((valor_iliquido > 20000) and (valor_iliquido <= 50000)) :
            impostos = valor_iliquido * impostos2
            print("Tem a pagar ao estado 25% do valor que arrecadou :€",impostos)

        if (valor_iliquido > 50000) :
            impostos = valor_iliquido * impostos3
            print("Tem a pagar ao estado 28%  :€",impostos)
        print("Valor liquido a receber : ",valor_iliquido -custo_limpeza - impostos)


   #Quartos de Vazios
if servico_desejado == "2":

        num_quarto = int(input("Indique o número do quarto  entre 1 e 100: "))


        if num_quarto<=0 or num_quarto >=100 :
            print("Indique o número do quarto por  entre 1 e 100: " )

        else:
            print("O numero  primo  ", num_quarto)

            num = 2
            while num <= num_quarto:
                primo = 1
                divisor = 2
                while divisor * divisor <= num:
                    if num % divisor == 0:
                        primo = 0
                    divisor += 1
                if primo:
                    print(num)
                num += 1




