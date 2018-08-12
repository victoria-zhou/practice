import math

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n ** p

cal = Calculator()
assert cal.power(2,5) == 32

# try:
#     cal.power(-1,0)
#     assert False, "you should not see this line"
# except ValueError:
#     assert True

# try:
#     cal.power(-2,5)
#     assert False, "you should not see this line"
# except ValueError:
#     assert True

# try:
#     cal.power(-1,-3)
#     assert False, "you should not see this line"
# except ValueError:
#     assert True

# try:
#     cal.power(1,-3)
#     assert False, "you should not see this line"
# except ValueError:
#     assert True

# try:
#     cal.power(0,-2)
#     assert False, "you should not see this line"
# except ValueError:
#     assert True

# short method for abv
for n,p in ((-1,0),(-2,5),(-1,-3),(1,-3),(0,-2)):
    try:
        cal.power(n,p)
        assert False, "You should not see this line"
    except ValueError as err:
        print(err)
        assert True # this can be omitted or type pass, it's here for users to understand the logic of the codes.