# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

class MyQueue(object):
    def __init__(self):
        self.fifo = []
    
    def peek(self):
        if self.fifo:
            return self.fifo[0]
        return None
    
    def pop(self):
        if self.fifo:
            res = self.fifo[0]
            self.fifo = self.fifo[1:]
            return res
        else:
            return None
            
    def put(self, value):
        self.fifo.append(value)
    
    def __str__(self):
        return str(self.fifo)
        

queue = MyQueue()
print('Please type integer, one or two together') // know how to use this
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())