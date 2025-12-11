from functools import cache

with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    
data = [line.split(" ") for line in lines]

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

def findAllPaths(startNode : Node, endNode : Node):       
        @cache
        def searchPaths(node : Node, seenFFT : bool, seenDAC : bool) -> int:
            if node == endNode:
                return 1 if seenFFT and seenDAC else 0
            else:
                curSum = 0
                for child in node.getChildren():
                    curSum += searchPaths(child, seenFFT or child.getValue() == 'fft', seenDAC or child.getValue() == 'dac')
                return curSum
        return searchPaths(startNode, False, False)

# Goal: find all ways I can travel from a starting node to an ending node with constraints
nodes = parseData(data)

svrNode = nodes["svr"]
outNode = nodes["out"]
requiredNodes = [nodes['dac'], nodes['fft']]

pathsCount = findAllPaths(svrNode, outNode)
print("All different paths from 'svr' to 'out that include 'dac' and 'fft':", pathsCount)    
    