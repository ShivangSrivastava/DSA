class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data =data
        self.children = []

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        indent = " " * self.get_level()
        prefix = ""

        if self.get_level():
            prefix = "|--- "
        
        prefix = indent + prefix

        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

