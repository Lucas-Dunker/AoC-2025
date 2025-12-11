with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    
data = [line.split(" ") for line in lines]

def parseData(data):
    nodes = {}
    for line in data:
        curNode = Node(line[0][0:-1])
        nodes[curNode.getValue()] = curNode
        
    nodes["out"] = Node("out")
        
    for line in data:
        curNode = nodes[line[0][0:-1]]
        for child in line[1:]:
            curNode.add_child(nodes[child])
    return nodes    

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, list_of_children):
        for child in list_of_children:
            self.add_child(child)
            
    def getValue(self):
        return self.value
    
    def getChildren(self):
        return self.children
    
    def __str__(self) -> str:
        return f'{self.value} {self.children}'
    
    def __repr__(self) -> str:
        return f'{self.value} {self.children}'

def findAllPaths(startNode : Node, endNode : Node):
        pathsCount = 0
        queue = [startNode]
        
        while queue:
            curNode = queue.pop()
            for child in curNode.getChildren():
                if child == endNode:
                    pathsCount += 1
                else:
                    queue.append(child)
            
        return pathsCount

# Goal: find all ways I can travel from a starting node to an ending node
nodes = parseData(data)

youNode = nodes["you"]
outNode = nodes["out"]

pathsCount = findAllPaths(youNode, outNode)
print("All different paths from 'you' to 'out:", pathsCount)    
    