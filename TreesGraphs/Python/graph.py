# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:45:04 2020

@author: ankan
"""
from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbor_nodes = list()
    def changeVal(self, val):
        self.val = val
    def addNodeWithVal(self,val):
        self.neighbor_nodes.append(GraphNode(val))
    def addNode(self,node):
        self.neighbor_nodes.append(node)
    def getNeighbors(self):
        return self.neighbor_nodes
    def getValue(self):
        return self.val

class Graph:
    def __init__(self, root):
        self.root = root

    def bfs(self,key):
        nodes = deque()
        visited = list()
        nodes.append(self.root)
        
        while(len(nodes) != 0):
            currNode = nodes.popleft()
            
            if key == currNode.getValue():
                return True
            
            for i in currNode.getNeighbors():
                if i not in visited:
                    nodes.append(i)
                    visited.append(i)
                    
        return False
                    
# main part

# graph visualized
"""
    5 -> 4 -> 3
           -> A
           -> B
      -> 2 -> 8
           -> 9
      <-> F

"""      
head = GraphNode(5)
child1 = GraphNode(4)
child2 = GraphNode(2)
child3 = GraphNode('F')
head.addNode(child1)
head.addNode(child2)
child2.addNodeWithVal(8)
child2.addNodeWithVal(9)
child1.addNodeWithVal(3)
child1.addNodeWithVal('A')
child1.addNodeWithVal('B')
head.addNode(child3)
child3.addNode(head) # 5 <-> 'F'

g = Graph(head)
print(g.bfs('15'))