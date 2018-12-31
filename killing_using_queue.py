import sys

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def killing(arr, n):

    to_kill = Queue()

    for person in arr:
        to_kill.enqueue(person)


    while to_kill.size() > 1:
        for i in range(n):
            to_kill.enqueue(to_kill.dequeue())

        to_kill.dequeue()

    return to_kill.dequeue()


print(killing([4,2,3,5], 2))