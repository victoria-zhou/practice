import sys

class Stack:
    def __init__(self):
        self.a_stack = []

    def pop(self):
        if self.a_stack:   # needs to check if the stack is empty first
            return self.a_stack.pop()

    def push(self, integer):
        self.a_stack.append(integer)



if __name__ == '__main__':
    line_list = []
    for line in sys.stdin:
        line_list = [int(x) for x in line.split()] # split() by default is sppliting by a space

    a_stack = Stack()

    for number in line_list:
        a_stack.push(number)

    size = len(line_list)
    times = 0
    
    # if size % 2 == 0:
    #     times = size // 2
    # else:
    #     times = (size // 2) + 1 //  this is not appropriate as it is not very clear compared to below

    result = []
    for i in range(size):
        if i % 2 == 0:
            result.append(a_stack.pop())
        else:
            a_stack.pop()

    print(result)

