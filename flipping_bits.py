# Complete the flippingBits function below.
# https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
def flippingBits(n):
    bin_n = bin(n)[2:]
    num_of_zeros = 32 - len(bin_n)
    bin_n = '0' * num_of_zeros + bin_n
    flip_bin_n = ''.join('1' if i == '0' else '0' for i in bin_n)
    # print(bin_n, flip_bin_n)
    return int(flip_bin_n, 2)
    
