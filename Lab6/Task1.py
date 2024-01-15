# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:17:28 2023

@author: TORA TECH
"""

class Node:
    def __init__(self, labelName, heuristicCost):
        self.labelName = labelName
        self.heuristicCost = heuristicCost
        self.actualCost = float('inf')
        self.parent = None
    
    def __lt__(self, other):
        return (self.actualCost + self.heuristicCost) < (other.actualCost + other.heuristicCost)

def AStar(graph, start, goal):
    openSet = [start]
    closedSet = set()
    
    while openSet:
        openSet.sort()
        currentNode = openSet.pop(0)
        
        if currentNode.labelName == goal.labelName:
            path = []
            while currentNode:
                path.insert(0, currentNode.labelName)
                currentNode = currentNode.parent
            return path
        
        closedSet.add(currentNode.labelName)
        
        for neighbor, distance in graph[currentNode]:
            if neighbor.labelName in closedSet:
                continue
            
            new_cost = currentNode.actualCost + distance
            if new_cost < neighbor.actualCost:
                neighbor.actualCost = new_cost
                neighbor.parent = currentNode
                
                if neighbor not in openSet:
                    openSet.append(neighbor)
    
    return None

#Heuristic Values
A = Node('A', 10)
B = Node('B', 8)
C = Node('C', 5)
D = Node('D', 7)
E = Node('E', 3)
F = Node('F', 6)
G = Node('G', 5)
H = Node('H', 3)
I = Node('I', 1)
J = Node('J', 0)

#Actual Values
graph = {
    A: [(B, 6), (F, 3)],
    B: [(A, 6), (D, 2), (C, 3)],
    C: [(B, 3), (D, 1), (E, 5)],
    D: [(B, 2), (C, 1), (E, 8)],
    E: [(C, 5), (D, 8), (I, 5), (J, 5)],
    F: [(A, 3), (G, 1), (H, 7)],
    G: [(I, 3), (F, 1)],
    H: [(F, 7), (I, 2)],
    I: [(G, 3), (H, 2), (E, 5), (J, 3)],
    J: [(E, 5), (I, 3)]
}

#Initial Cost is zero
A.actualCost = 0
path = AStar(graph, A, J)

if path:
    print("Path:", " -> ".join(path))
else:
    print("There is no path.")