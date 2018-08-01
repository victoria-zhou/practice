print('Please type the number of lines of characteristics and then type string, one at a time till the number typed')
for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])