class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n+1):
            if n % i == 0:
                sum = sum +i
        return sum 

cal = Calculator()
print(cal.divisorSum(6))
print("I implemented: " + type(cal).__bases__[0].__name__)


# class A:
#     def __init__(self):
#         print('A')


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('B')


# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('C')


# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print('D')


# d = D()
# print(type(d).__bases__[0].__name__)
# print(type(d).__mro__)