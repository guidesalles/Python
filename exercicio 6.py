def conversao (hora,minuto):
    if hora > 12:
        hora -= 12
        print(str(hora) + ":"+ str(minuto) +"PM")
    else:
        print(str(hora) + ":" + str(minuto) + "AM")

x =int(input('Qual a hora? '))
y= int(input('Quantos minutos? '))

conversao(x,y)
