import sys


class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(0)

    def remove_front(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        result = []
        for item in self.items:
            to_add = str(item)
            result.append(to_add)

        return ' '.join(result)


def killing(arr, m):
    result = []
    count = 1
    all_left = Deque()

    for each in arr:
        all_left.add_rear(each)

    print(all_left)


    while not all_left.is_empty():
        if count < m:
            all_left.add_rear(all_left.remove_front())
            count += 1
        else:
            result.append(all_left.remove_front())
            count = 1

    return result 


arr = []
for i in range(10):
    arr.append(i)

print(arr)

print(killing(arr, 3))

