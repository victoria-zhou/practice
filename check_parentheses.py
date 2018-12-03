class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def check_parenthese(paren_string):
    openings = Stack()
    balanced = True
    index = 0

    while index < len(paren_string) and balanced:
        if paren_string[index] == '(':
            openings.push(paren_string[index])
        else:
            if openings.is_empty():
                balanced = False
            else:
                openings.pop()

        index += 1


    if balanced and openings.is_empty():
        return True
    else:
        return False


print(check_parenthese('(())'))
print(check_parenthese('(((('))



