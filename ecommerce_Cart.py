cart = []

cart.append(("t-shirt", 25))
cart.append(("wallet", 20))
cart.append(("backpack", 50))
cart.append(("jacket", 100))
cart.append(("cap", 15))

checkout = [y for x,y in cart]

print(sum(checkout))