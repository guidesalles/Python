import random

number = random.randrange(1, 101)

guess = input("Chute um número(1 até 100): ")

if guess == number:
    print("Correct")

else:
    print("worng")
    print(f'o número correto é {number}')