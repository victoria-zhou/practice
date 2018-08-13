import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)
    
    def popCharacter(self):
        return self.stack.pop()
        
    def dequeueCharacter(self):
        return self.queue.pop()

sol = Solution()
sol.pushCharacter(2)
sol.pushCharacter('y')
sol.pushCharacter('z')

sol.enqueueCharacter(2)
sol.enqueueCharacter('y')
sol.enqueueCharacter('z')


print(sol.stack)
print(sol.queue)

assert sol.popCharacter() == 'z'
assert sol.dequeueCharacter() == 2
