class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_list:
    def __init__(self):
        self.head = self.tail = None

    def insert_node(self, head, data):
        new_node = Node(data)
        if not head:
            self.head = self.tail = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next 
            current_node.next = new_node 
            self.tail = new_node 

    def remove_duplicates(self,head):
        if not head:
            return 
        else:
            data_list = [] 
            current_node = head
            data_list.append(head.data) 
            while current_node.next:
                if current_node.next.data not in data_list:
                    data_list.append(current_node.next.data)
                    current_node = current_node.next 
                else:
                    current_node.next = current_node.next.next
        return head

    def __repr__(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return ' '.join(map(str, result))


linked_list = Singly_Linked_list()
linked_list.insert_node(linked_list.head, 5)
linked_list.insert_node(linked_list.head, 5)
linked_list.insert_node(linked_list.head, 6)
linked_list.insert_node(linked_list.head, 5)
linked_list.insert_node(linked_list.head, 8)
linked_list.insert_node(linked_list.head, 19)
linked_list.insert_node(linked_list.head, 6)

print(linked_list)

linked_list.remove_duplicates(linked_list.head)

print(linked_list)
