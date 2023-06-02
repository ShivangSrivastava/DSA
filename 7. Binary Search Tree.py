class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data==data:
            return -1
        if self.data<data:
            if self.right:
                self.right.add_child(data)
                return
            self.right=BinarySearchTreeNode(data)
            return
        if self.data>data:
            if self.left:
                self.left.add_child(data)
                return
            self.left = BinarySearchTreeNode(data)
            return

    def search(self, val):
        if self.data==val:
            return True
        if self.data<val:
            self.right.search(val)
        elif self.data > val:
            self.left.search(val)
        return False
    
    def in_order_traversal(self):
        arr = []
        if self.left:
            arr += self.left.in_order_traversal()
        arr.append(self.data)
        if self.right:
            arr+=self.right.in_order_traversal()
        return arr

    def delete(self, val):
        if self.data < val:
            if self.right:
                self.right = self.right.delete(val)
        elif self.data>val:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.left is None and self.right is None:
                self.data = None
            elif self.left:
                return self.left
            else:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self
            

    def find_max(self):
        return self.right.find_max() if self.right else self.data

    def find_min(self):
        return self.left.find_min() if self.left else self.data
    