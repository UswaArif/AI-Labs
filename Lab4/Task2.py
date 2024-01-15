# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:30:02 2023

@author: TORA TECH
"""

def breadth_first_search(graph, start, goal):
    '''
    set function is used to keep track nodes will not be revisited '''
    visited = set()
    to_visit = [(start, [])]

    while to_visit:
        node, path = to_visit.pop(0)
        if node not in visited:
            visited.add(node)

            if node == goal:
                return path + [node]

            for neighbor in graph[node]:
                if neighbor not in visited:
                    to_visit.append((neighbor, path + [node]))

    return None  

def depth_first_search(graph, start, goal):
    visited = set()
    to_visit = [(start, [])]

    while to_visit:
        node, path = to_visit.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return path + [node]

            for neighbor in graph[node]:
                if neighbor not in visited:
                    to_visit.append((neighbor, path + [node]))

    return None  


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

start = 0
goal = 3

bfs_result = breadth_first_search(graph, start, goal)
dfs_result = depth_first_search(graph, start, goal)

print("Breadth-First Search:", bfs_result)
print("Depth-First Search:", dfs_result)

