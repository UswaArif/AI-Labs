# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:02:28 2023

@author: TORA TECH
"""

import numpy as np

grid_size = 4
num_actions = 4
num_states = grid_size * grid_size

grid = [
    'SFFF',
    'FHFF',
    'FFFF',
    'HFFG'
]

rewards = {
    'S': 0,
    'F': -0.1,
    'H': -1,
    'G': 1
}

P = np.zeros((num_states, num_actions, num_states))

def get_next_state(state, action):
    row, col = state // grid_size, state % grid_size
    if grid[row][col] == 'G':
        return state
    if grid[row][col] == 'H':
        return state
    if action == 0:
        row = max(row - 1, 0)
    elif action == 1:
        row = min(row + 1, grid_size - 1)
    elif action == 2:
        col = max(col - 1, 0)
    elif action == 3:
        col = min(col + 1, grid_size - 1)
    return row * grid_size + col
#v = value function of each state
V = np.zeros(num_states)

discount_factor = 0.99

num_iterations = 1000
for _ in range(num_iterations):
    V_next = np.zeros(num_states)
    for state in range(num_states):
        if grid[state // grid_size][state % grid_size] in ['H', 'G']:
            V_next[state] = rewards[grid[state // grid_size][state % grid_size]]
        else:
            max_q_value = float("-inf")
            for action in range(num_actions):
                next_state = get_next_state(state, action)
                q_value = rewards[grid[next_state // grid_size][next_state % grid_size]] + discount_factor * V[next_state]
                if q_value > max_q_value:
                    max_q_value = q_value
            V_next[state] = max_q_value
    V = V_next

optimal_policy = np.zeros(num_states, dtype=int)
for state in range(num_states):
    if grid[state // grid_size][state % grid_size] not in ['H', 'G']:
        max_action = None
        max_q_value = float("-inf")
        for action in range(num_actions):
            next_state = get_next_state(state, action)
            q_value = rewards[grid[next_state // grid_size][next_state % grid_size]] + discount_factor * V[next_state]
            if q_value > max_q_value:
                max_q_value = q_value
                max_action = action
        optimal_policy[state] = max_action



print("Optimal Policy:")
for row in range(grid_size):
    for col in range(grid_size):
        state = row * grid_size + col
        action = optimal_policy[state]
        if grid[row][col] == 'S':
            print("S ", end="")
        elif grid[row][col] == 'H':
            print("H ", end="")
        elif grid[row][col] == 'G':
            print("G ", end="")
        else:
            if action == 0:
                print("U ", end="")
            elif action == 1:
                print("D ", end="")
            elif action == 2:
                print("L ", end="")
            elif action == 3:
                print("R ", end="")
    print()