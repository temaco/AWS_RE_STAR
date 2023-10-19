n_quarto= int(input("Indica o numero do quarto:"))
n_reserva= int(input("Indica os dias reservados:"))
custo_diario = 200
limpeza = 15
descontos_fiscais = 0.3
valor_iliquido_reserva = 0
custo_total_limpeza = 0
valor_liquido_do_quarto = 0
valor_totalFiscal = 0


#Iniciacao da declaracao O valor ilíquido a receber pelas reservas totais e o custo total da limpeza
valor_iliquido_reserva = n_reserva * custo_diario
custo_total_limpeza = n_quarto * limpeza
valor_totalFiscal = valor_iliquido_reserva - custo_total_limpeza * descontos_fiscais
valor_liquido_do_quarto = valor_iliquido_reserva - custo_total_limpeza * valor_totalFiscal
print("Valor ilíquido a receber pelas reservas totais e de : €",valor_iliquido_reserva)
print("Total do custo da limpeza: €",custo_total_limpeza)
print("Total do custo fiscal para o Estado e de : €", valor_totalFiscal)
print("valor liquido do quarto e de : €", valor_liquido_do_quarto)

#difinir os precos dos quartos com base a sua topologia
while custo_diario >200:
    print("quarto reservado",)





#Descontos fiscais
if valor_iliquido_reserva <= 20000:
    descontos_fiscais = valor_iliquido_reserva * 0.3
    print(" o desccontos fiscal e de :  €", descontos_fiscais)
if custo_diario >= 20000 and custo_diario <= 50000:
    descontos_fiscais = custo_diario * 0.5
    print("Descontos fiscais  e de :  €", descontos_fiscais )
    if custo_diario >5000:
        descontos_fiscais = custo_diario * 0.28
        print("Descontos fiscais e de :", descontos_fiscais)
        print(" valor liquido e de :", custo_diario-limpeza-descontos_fiscais)


