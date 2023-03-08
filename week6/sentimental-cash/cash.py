# TODO
from cs50 import get_float


def main():
    # make the amount to cents
    cents = get_cents() * 100
# deduct amount from each calculation
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
# calculate total number of coins
    coins = quarters + dimes + nickels + pennies
# print number of coins in int form
    print(int(coins))


def get_cents():
    # take amount owed if its a number above 0
    while True:
        amount = get_float("Change owed: ")
        if amount > 0:
            break
    return amount


def calculate_quarters(cents):
    x = cents // 25
    return x


def calculate_dimes(cents):
    y = cents // 10
    return y


def calculate_nickels(cents):
    z = cents // 5
    return z


def calculate_pennies(cents):
    k = cents // 1
    return k


main()