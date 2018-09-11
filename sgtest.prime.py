
def  remainderSumSquares(input):
    summation  = sum(i*i for i in range(input + 1))
    # print(summation)
    return summation % 3

def  NstPrimeNumber(input):
    prime_list = [2]
    num = 3
    while len(prime_list) < input:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]