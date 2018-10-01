# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

# Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

# For example, there are  flavors having . Together they have  to spend. They would purchase flavor ID's  and  for a cost of . Use  based indexing for your response.


def what_flavors(cost, money):
#     check = []
#     size = len(cost)
#     for index in range(size):
#         ice1 = cost[index]
#         ice2 = money - ice1
        
#         if ice2 in check:
#             print(cost.index(ice2)+1, index + 1)
#         else:
#             check.append(ice1)
    
    pair = {}
    for index, price in enumerate(cost):  # dictinory has O(1) complexity compared to above, which has O(n) complexity, thus time out
        if price in pair:
            return [pair[price][1], index+1] # know how to return a list. 
        else:
            pair[money-price] = price, index+1



assert what_flavors([1, 4, 5, 3, 2], 4) == [1, 4]
assert what_flavors([2, 2, 4, 3], 4) == [1, 2]