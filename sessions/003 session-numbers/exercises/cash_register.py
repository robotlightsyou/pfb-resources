#! /usr/bin/env python3
'''

print("How much change is owed?")
amount = input("> ")
# coerce to int for easier math
amount = int(round(float(amount) * 100))
print(amount)

coins = [1,5,10,25]
total = 0

for coin in coins[::-1]:
    if amount > 25:
        total = amount / 25
        amount %= 25
    if amount > 10:
        total += amount / 10
        amount %= 10
    if amount > 5:
        total += amount / 5
        amount %= 5
    # no math for pennies
    if amount:
        total += amount

print(total)

i'''
#! /usr/bin/env python3


print("How much change is owed?")
amount = input("> ")
# amount = '.41'
# coerce to int for easier math
amount = int(round(float(amount) * 100))
# print(amount)

coins = [1,5,10,25]
total = 0

for coin in coins[::-1]:
    if amount >= coin:
        total += amount // coin
        amount %= coin

print(total)