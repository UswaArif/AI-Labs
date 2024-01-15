# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:37:22 2023

@author: TORA TECH
"""

import heapq

class Node:
    def __init__(self, state, cost):
        self.state = state  
        self.cost = cost    

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(graph, start, goal):
    openSet = [Node(start, 0)]
    heapq.heapify(openSet)

    closedSet = set()

    while openSet:
        currentNode = heapq.heappop(openSet)

        if currentNode.state == goal:
            return currentNode.cost  

        closedSet.add(currentNode.state)

        for neighbor, neighborCost in graph[currentNode.state]:
            if neighbor not in closedSet:
                heapq.heappush(openSet, Node(neighbor, currentNode.cost + neighborCost))

    return None


graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('C', 2), ('D', 3)],
    'C': [('D', 1)],
    'D': []
}

start = 'A'
goal = 'D'

result = uniform_cost_search(graph, start, goal)

if result is not None:
    print("Lowest cost from A to D: ",result)
else:
    print("No path found.")