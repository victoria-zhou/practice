class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data, end =' ')
            current = current.next

    def insert(self, head, data): 
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head

mylist= Solution()
print('Please give an integer')
T=int(input())
head=None
for i in range(T):
    print('Please give', T, 'intergers, one at a time')
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);    