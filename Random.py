import random

def embaralho (x):
    x = random.sample(x, len(x))
    print(x)

nome = input("Digite uma palavra: ")

embaralho(nome)
