print('********************* calculadora *****************')

print("Selecione a opção desejada:")
print('1 - soma')
print('2- subtração')
print('3- Multi')
print('4- div')
opcao = input("Qual opção deseja(1,2,3 ou 4)? ")

if opcao == "1":
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('digite o segundo número: '))
    Soma = num1 + num2
    print(Soma)

if opcao == "2":
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('digite o segundo número: '))
    Sub = num1 - num2
    print(Sub)

if opcao == "3":
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('digite o segundo número: '))
    multi = num1 * num2
    print(multi)

if opcao == "4":
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('digite o segundo número: '))
    div = num1 / num2
    print(div)