def findPhoneNumber(phoneBook, name):
    if name in phoneBook:
        print('%s=%s' %(name, phoneBook[name]))
    else:
        print('Not found')
    
    
    
if __name__ == '__main__':
    phoneBook = {}
    size = int(input())
    for i in range(size):
        namePhone = input()
        name, phone = namePhone.split()
        phoneBook[name] = phone
    
    for i in range(size):
        findPhoneNumber(phoneBook, input())