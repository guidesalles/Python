def imprimeLinha(listanumeros):
    linha = ""
    for i in listanumeros:
        linha = linha + str(i) + " "
    print(linha)


num = int(input('escolha um número: '))

intervalonumeros = list(range(1, num + 1))

for i in intervalonumeros:
    meuintervalo = list(range(1,i+1))
    imprimeLinha(meuintervalo)








