class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head

        index = 0
        while current_node:
            if current_node.data == data:
                return index

            index += 1
            current_node = current_node.next

        return -1

    def display(self):
        if self.is_empty():
            print("Linked List is empty")
        else:
            current_node = self.head
            lltr = ""
            while current_node:
                lltr = f"{lltr}{current_node.data} --> "
                current_node = current_node.next
            print(lltr)
