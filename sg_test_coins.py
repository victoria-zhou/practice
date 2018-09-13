

def number_of_coins(amount):
    coins = 0
    integ, amount = map(int, str(amount).split('.'))
    if integ > 0:
        if integ % 2 == 0:
            coins += integ /2
        else:
            coins += int(integ/2) + 1  # know how to use int()

    while amount:
        if amount >= 50:
            amount -= 50
            coins += 1

        elif amount >= 20:
            amount -= 20
            coins += 1

        elif amount >= 10:
            amount -= 10
            coins += 1

        elif amount >= 5:
            amount -= 5
            coins += 1

        elif amount >= 2:
            amount -= 2
            coins += 1

        elif amount >= 1:
            amount -= 1
            coins += 1

    return coins

assert number_of_coins(6.03) == 5
assert number_of_coins(31.68) == 21
assert number_of_coins(15.0) == 8



