class Stack:

    def __init__(self):
        self.a_stack = []

    def push(self, item):
        self.a_stack.append(item)

    def __str__(self):
        return ''.join(reversed(self.a_stack))

stack = Stack()

def to_string(n, base):
    convert_string = '0123456789'

    if n < base:
        stack.push(convert_string[n])

    else:
        stack.push(convert_string[n % base])
        to_string(n // base, base)

to_string(325, 4)
print(stack)