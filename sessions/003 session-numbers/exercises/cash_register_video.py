#! /usr/bin/env python3

'''
write a function that will ask for the
user for input which will be an amount
of money, then return the minimum 
number of coins.
'''

user_coins = [25, 10, 5, 1]
# print return of get_change
def main():
    print(get_change())

def get_change():

    # take input
    print("How much change is owed?")
    amount = input("> ")
    # modify input from integer
    amount = int(float(amount) * 100)

    # find least number of coins
    # coins = 0 
    # coins += amount // 25 # -> 1
    # amount %= 25 # -> 16
    # coins += amount // 10 # -> 1
    # amount %= 10 # -> 6
    # coins += amount // 5 # -> 1
    # amount %= 5 # 1
    # coins += amount
    # return coins

    # find least number of coins
    total_coins = 0 
    for coin in user_coins:
        total_coins += amount // coin
        amount %= coin
    return total_coins



if __name__ == '__main__':
    main()
    


'''
.31
[25, 10, 1]
1 '25', 6 '1'
3 '10', 1 '1'
'''