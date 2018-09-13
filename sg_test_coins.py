def numberOfCoins(amount):
    coins = 0
    integ, amount = map(int, str(amount).split('.'))
    if integ > 0:
        if integ % 2 == 0:
            coins += integ / 2
        elif integ > 0 :
            coins += int(integ / 2) + 1
        # amount = amount - integ
    
    print(integ, amount)
    while amount:
        print(amount)
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