








def decodeHuff(root, s):
    to_visit = root
    result = []
    for letter in s:
        num = int(letter)
        if num == 1:
            to_visit = to_visit.right
        elif num == 0:
            to_visit = to_visit.left
        if to_visit.right == to_visit.left == None:
            result.append(to_visit.data)
            to_visit = root
    
    print(''.join(result))