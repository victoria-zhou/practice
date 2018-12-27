import sys

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'{self.value}'

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if not self.head:
            self.head = Node(item, None, None)
            self.head.prev = self.head
            self.head.next = self.head
            self.tail = self.head
        else:
            node = Node(item, self.head, self.tail)
            self.tail.next = node
            self.tail = node
            self.head.prev = self.tail

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def __str__(self):
        result = []
        node = self.head
        while(node != self.tail):
            result.append(str(node.value))
            node = node.next

        result.append(str(node.value))
        return ' '.join(result)


cll = CircularLinkedList()
for a in range(10):
    cll.add(a)

print(cll)
order = []
count = 0
node = cll.head
while(cll.head != cll.tail):
    count += 1
    if count == 3:
        order.append(node.value)
        cll.remove(node)
        count = 0

    node = node.next
order.append(node.value)
print(order)
