def somaimposto (x,y):
    total = x * (1+(y/100))
    print(total)


custo = int(input('Qual o valor do item? '))


imposto = int(input('Qual o valor do imposto(em %)? '))

somaimposto(custo,imposto)
