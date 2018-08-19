def str1_is_rot_str2(str1, str2):
    if not len(str1) == len(str2):
        return False
    
    if str1 == str2:
        return False 
    
    else:
        size = len(str1)
        for i in range(size):
            if str1[i:] + str1[:i] == str2:
                return True
                
    return False


assert not str1_is_rot_str2('qwer', 'qwer')
assert not str1_is_rot_str2('qwe4', 'qwer')
assert str1_is_rot_str2('qwer', 'rqwe')
assert not str1_is_rot_str2('qwer', 'rqe')
