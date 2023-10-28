from Edge import Edge
from Feature import Feature
class IndoorNav:

    def __init__(self):
        self.nodes = list()
        self.edges = list()
        

    def add_edge(self, edge: Edge):
        if(edge.lm not in self.nodes):
            self.nodes.append(edge.lm)
        if(edge.ft not in self.nodes):
            self.nodes.append(edge.ft)
        self.edges.append(edge)

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1.__eq__(node2):
            return path

        for node in self.nodes:
            if node not in path:
                if self.common_edge(node, node1):
                    new_path = self.find_path(node, node2, path)
                    if new_path:
                        return new_path
        return None
    
    def common_edge(self, node1, node2):
        result = False
        i = 0
        while(not result and i<len(self.edges)):
            curr = self.edges[i]
            if((node1.__eq__(curr.lm) and node2.__eq__(curr.ft)) or (node2.__eq__(curr.lm) and node1.__eq__(curr.ft))):
                result = True
            i+=1
        return result
    
    def search(self, f):
        answer = list()
        for edge in self.edges:
            if edge.lm.__eq__(f):
                answer.append(edge.ft)
            elif edge.ft.__eq__(f):
                answer.append(edge.lm)
        return answer
    
    def find_node_by_name(self, name):
        result = None
        for node in self.nodes:
            if(node.name == name):
                resule = node
        return result
    
    # def helper(self, en: Feature, answer: list[list(Feature)]):
    #     for x in answer:
    #         next_steps = self.search(x)
    #         for ft in next_steps:

        


    def print_path(self, path:list[Feature]):
        result = " START"
        
        for i in range(len(path)-1):
            result += "\n Go From " + path[i].name + " to " + path[i+1].name
        
        result += "\n END"

        return result
    
    