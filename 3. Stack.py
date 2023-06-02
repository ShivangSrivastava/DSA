
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise Exception("Pop from empty stack")
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        raise Exception("Stack is empty")
    
    def is_empty(self):
        return False if self.stack else True
    
    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        for i in list(self.stack)[::-1]:
            print(i, end=", ")
        print()
