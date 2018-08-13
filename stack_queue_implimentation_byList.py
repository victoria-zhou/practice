import sys

#---------------------- 1ST SOLUTION USING LIST -------------------------
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch): # know diff between append() and insert(index, ch), what is pop()?
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)
    
    def popCharacter(self):
        return self.stack.pop()
        
    def dequeueCharacter(self):
        return self.queue.pop()

sol = Solution()
sol.pushCharacter(2)
sol.pushCharacter('y') # character needs '', if nn '', would be an undefined variable
sol.pushCharacter('z')

sol.enqueueCharacter(2)
sol.enqueueCharacter('y')
sol.enqueueCharacter('z')


print(sol.stack) # dont forget () and sol.stack not self.stack
print(sol.queue)

assert sol.popCharacter() == 'z'
assert sol.dequeueCharacter() == 2

#----------------------- 2ND SOLUTION USING LINKED LIST ------------------------
class Node:                         # node in linkedlist only has data+next(single)+prev(doubly), here doubly is better
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:                   # linkedlist as a list, only has head + tail
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return f'{data}'

class Solution2:
    def __init__(self):
        self.stack = LinkedList()
        self.queue = LinkedList()
    
    def pushCharacter(self, ch): 
        new_node = Node(ch)
        if not self.stack.head:    # always remember to include none situation
            self.stack.head = new_node 
            self.stack.tail = new_node
        else:
            self.stack.tail.next = new_node
            new_node.prev = self.stack.tail
            self.stack.tail = new_node 
    
    def enqueueCharacter(self, ch):
        new_node = Node(ch)
        if not self.queue.head:
            self.queue.head = new_node 
            self.queue.tail = new_node
        else:
            new_node.next = self.queue.head
            self.queue.head.prev = new_node
            self.queue.head = new_node
    
    def popCharacter(self):
        # current_node = self.stack.head
        # self.stack.tail.prev.next = None
        #self.stack.tail.prev = None
        node = self.stack.tail
        self.stack.tail.prev.next = None
        self.stack.tail = self.stack.tail.prev
        return node.data
      
    def dequeueCharacter(self):
        # current_node = self.queue.head
        # self.queue.tail.prev.next = None
        # #self.queue.tail.prev = None
        node = self.queue.tail
        self.queue.tail.prev.next = None
        self.queue.tail = self.queue.tail.prev
        return node.data
    
sol1 = Solution2()
sol1.pushCharacter(2)
sol1.pushCharacter('y') # character needs '', if nn '', would be an undefined variable
sol1.pushCharacter('z')

sol1.enqueueCharacter(2)
sol1.enqueueCharacter('y')
sol1.enqueueCharacter('z')


print(sol1.stack) # stack is a linkedlist, which has data+reference to next node, meaning linkedlist is an object, 
                    # thus print(self.stack) returns memory address and needs to have def __repr__(self): so 
                    # when print(), it gives the contents of the object, here contents of linkedlist, stack and queue
print(sol1.queue) 

assert sol1.popCharacter() == 'z'
assert sol1.dequeueCharacter() == 2
