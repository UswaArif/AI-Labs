# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:38:46 2023

@author: TORA TECH
"""

import heapq

class Node:
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.depth = depth 
        self.cost = cost  

    def __lt__(self, other):
        return self.cost < other.cost

    def isGoal(self, goalState):
        return self.state == goalState

    def generateChildren(self, node):
        children = []
        empty_row, empty_col = divmod(node.state.index(0), 3)  
        #left,right,up ,down
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in moves:
            new_row, new_col = empty_row + dr, empty_col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:  
                newState = list(node.state)
                newState[empty_row * 3 + empty_col], newState[new_row * 3 + new_col] = newState[new_row * 3 + new_col], newState[empty_row * 3 + empty_col]
                action = f"Move {newState[empty_row * 3 + new_col]} to ({empty_row + dr}, {empty_col + dc})"
                childNode = Node(tuple(newState), parent=node, action=action, depth=node.depth + 1, cost=0)
                children.append(childNode)

        return children


class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def hScore(self, state):
        h = 0
        for i in range(3):
            for j in range(3):
                if state[i * 3 + j] != 0:
                    goal_row, goal_col = divmod(self.goal_state.index(state[i * 3 + j]), 3)
                    h += abs(i - goal_row) + abs(j - goal_col)
        return h

    def a_star_search(self):
        open_set = [Node(self.initial_state)]  
        closed_set = set()

        while open_set:
            current_node = heapq.heappop(open_set)  
            closed_set.add(current_node.state)

            if current_node.isGoal(self.goal_state):
                path = []
                while current_node:
                    path.append(current_node.action)
                    current_node = current_node.parent
                return path[::-1]  

            for child_node in current_node.generateChildren(current_node):
                if child_node.state not in closed_set:
                    child_node.cost = child_node.depth + self.hScore(child_node.state)
                    heapq.heappush(open_set, child_node)

        return None  

initial_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.a_star_search()

if solution:
    for step, action in enumerate(solution):
        print("Step ",step+1,": " , action)
else:
    print("No solution.")
