i = 4
d = 4.0
s = 'HackerRank'


import sys
n = 0
b = 0.0
t = ''

# Read and save an integer, double, and String to your variables.
print("Please input an integer number")
n = int(sys.stdin.readline())
print("Please input a float number")
b = float(sys.stdin.readline())
print("Please input a String")
t = sys.stdin.readline()

# Print the sum of both integer variables on a new line.
print(i + n)
# Print the sum of the double variables on a new line.
print(d + b)
# Concatenate and print the String variables on a new line
print(s + ' ' + t)
# The 's' variable above should be printed first.`