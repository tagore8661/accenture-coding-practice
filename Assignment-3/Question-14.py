# Question 14: Find Middle of Linked List
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

# Example: Find Middle of Linked List
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
print("Middle Element:", ll.find_middle())  # Output: 3