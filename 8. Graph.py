class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for key, value in edges:
            self.graph_dict.setdefault(key, []).append(value)
            
    
    def get_paths(self, start, end, path=None):
        if path is None:
            path = [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path + [node])
                paths.extend(new_path)

        return paths
        
    def get_shortest_path(self, start, end):
        paths = self.get_paths(start, end)
        if not paths:
            return []
        
        return min(paths, key=len)
