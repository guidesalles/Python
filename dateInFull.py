def dataPorExtenso (dia, x ,Ano):
    if x == "01":
        print(f'{dia} de Janeiro de {ano}')
    elif x== "02":
        print(f'{dia} de Fevereiro de {ano}')
    elif x == "03":
        print(f'{dia} de Março de {ano}')
    elif x == "04":
        print(f'{dia} de Abril de {ano}')
    elif x == "05":
        print(f'{dia} de Maio de {ano}')
    elif x == "06":
        print(f'{dia} de Junho de {ano}')
    elif x == "07":
        print(f'{dia} de Julho de {ano}')

    elif x == "08":
        print(f'{dia} de Agosto de {ano}')
    elif x == "09":
        print(f'{dia} de Setembro de {ano}')
    elif x == "10":
        print(f'{dia} de Outubro de {ano}')
    elif x == "11":
        print(f'{dia} de Novembro de {ano}')
    elif x == "12":
        print(f'{dia} de Dezembro de {ano}')
    else:
        print("NULL")

dia = input("qual dia é hj? ")
x = input("Qual mês? ")
ano = input("Qual ano? ")

dataPorExtenso(dia,x,ano)
