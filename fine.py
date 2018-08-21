import math
    
print('Please give actual book return date as dd mm yyyy')
ad, am, ay = [int(x) for x in input().split(' ')]
print('Please give expected book return date as dd mm yyyy')
ed, em, ey = [int(x) for x in input().split(' ')]

if (ed, em, ey) == (ad, am, ay):
    print(0)
elif (em, ey) == (am, ay):
    print(15*(ad - ed))
elif ay == ey:
    if am < em and ad < ed:
        print(0)
    else:
        print(500*(am - em))
elif ay > ey:
    print(10000)
else:
    print(0)
