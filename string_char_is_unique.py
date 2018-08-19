
#check whether a string as unique characteristics

# using additional data structure set
def is_unique(str):
    set1 = set(str)
    return len(set1) == len(str)


assert is_unique('adsba') == False
assert is_unique('adsbe') == True
assert is_unique('ad11a') == False
assert is_unique('ad123') == True


# no extra data structure used

def whether_unique(str):
    set1 = []
    for char in str:
        if char in set1:
            return False
        else:
            set1.append(char)
    return True

assert whether_unique('adsba') == False
assert whether_unique('adsbe') == True
assert whether_unique('ad11a') == False
assert whether_unique('ad123') == True 
