from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def is_empty(self):
        return False if self.queue else True
    
    def enqueue(self,item):
        self.queue.appendleft(item)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        raise Exception("Dequeue from empty queue")
    
    def front(self):
        if self.queue:
            return self.queue[0]
        raise Exception("Queue is empty")

    def size(self):
        return len(self.queue)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i in list(self.queue)[::-1]:
            print(i, end=", ")
        print()
