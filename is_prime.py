import math

print('-------- Method One, Big-O is O(sqrt(n))-------')
def is_prime(n):
    if n <= 1:
        return 'Not prime'
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

print('Please give an integer')
size = int(input())
for i in range(size):
    n = int(input())
    print(is_prime(n))


print('--------Method Two, Big-O is O(n)-------')
def is_prime2(n):
    if n == 1:
        return 'Prime'
    for i in range(2, n):
        if n % i == 0:
            return 'Not prime'
            break
    return 'Prime'

assert is_prime2(5) == 'Prime'
assert is_prime2(4) == 'Not prime'
assert is_prime2(1) == 'Prime'
#assert is_prime2(2) == 'Prime'
print(is_prime2(2))

