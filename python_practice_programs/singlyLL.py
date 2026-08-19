class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node    

    def delete_node(self, key):
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Node with data", key, "not found.")
            return
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                print("Node with data", key, "found.")
                return True
            current_node = current_node.next
        print("Node with data", key, "not found.")
        return False            
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_beginning(5)
    sll.display()  # Output: 5 -> 10 -> 20 -> None
    sll.search(10)  # Output: Node with data 10 found.
    sll.delete_node(10)
    sll.display()  # Output: 5 -> 20 -> None
    sll.search(10)  # Output: Node with data 10 not found.   
    sll.reverse()        
    sll.display()  # Output: 20 -> 5 -> 
    print("Length of the linked list:", sll.length())  # Output: Length of the linked list: 2gh 