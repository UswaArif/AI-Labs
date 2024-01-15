# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:21:18 2023

@author: TORA TECH
"""

import numpy as np

class ConnectFourGame(object):
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.EMPTY = 0
        self.PLAYER_ONE = 1
        self.PLAYER_TWO = 2

    def startState(self):
        return self.board

    def actions(self, state):
        valid_cols = []
        for col in range(self.cols):
            if self.is_valid_location(state, col):
                valid_cols.append(col)
        return valid_cols

    def succ(self, state, action, player):
        new_board = state.copy()
        self.drop_piece(new_board, action, player)
        return new_board

    def is_valid_location(self, board, col):
        return board[self.rows - 1][col] == self.EMPTY

    def drop_piece(self, board, col, piece):
        for r in range(self.rows):
            if board[r][col] == self.EMPTY:
                board[r][col] = piece
                break

    def winning_move(self, board, piece):
        # Check horizontally
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if np.all(board[r, c:c + 4] == piece):
                    return True

        # vertical checking
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if np.all(board[r:r + 4, c] == piece):
                    return True

        # positive check
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if np.all(board[r:r + 4, c:c + 4].diagonal() == piece):
                    return True

        # negative sloped diagonals
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if np.all(np.fliplr(board[r:r + 4, c:c + 4]).diagonal() == piece):
                    return True

        return False

    def isEnd(self, board):
        return self.winning_move(board, self.PLAYER_ONE) or self.winning_move(board, self.PLAYER_TWO) or len(self.actions(board)) == 0

    def utility(self, board):
        if self.winning_move(board, self.PLAYER_ONE):
            return 1  
        elif self.winning_move(board, self.PLAYER_TWO):
            return 2  
        else:
            return 0  

    def player(self, board):
        if np.sum(board == self.EMPTY) % 2 == 0:
            return self.PLAYER_ONE
        else:
            return self.PLAYER_TWO

def simplePolicy(game, state):
    action = np.random.choice(game.actions(state))
    print('simplePolicy: state {} => action {}'.format(state, action))
    return action

def humanPolicy(game, state):
    while True:
        print('humanPolicy: \n Enter move for state \n {} (0-6):'.format(state))
        action = int(input().strip())
        if action in game.actions(state):
            return action

def minimaxPolicy(game, state):
    def minimax(board, depth, alpha, beta, maximizing_player):
        valid_locations = game.actions(board)
        is_terminal = game.isEnd(board)

        if depth == 0 or is_terminal:
            if is_terminal:
                return (None, game.utility(board))
            else:
                return (None, game.utility(board))

        if maximizing_player:
            value = -np.Inf
            column = np.random.choice(valid_locations)
            for col in valid_locations:
                new_board = game.succ(board, col, game.PLAYER_TWO)
                _, new_score = minimax(new_board, depth - 1, alpha, beta, False)
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = np.Inf
            column = np.random.choice(valid_locations)
            for col in valid_locations:
                new_board = game.succ(board, col, game.PLAYER_ONE)
                _, new_score = minimax(new_board, depth - 1, alpha, beta, True)
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    action, _ = minimax(state, 4, -np.Inf, np.Inf, True)
    print('minimaxPolicy: state {} => action {}'.format(state, action))
    return action

def print_winner(player):
    if player == 1:
        print("Player 1 (Human) wins!")
    elif player == 2:
        print("Player 2 AI wins!")
    else:
        print("It's a tie!")

game = ConnectFourGame()

policies = {
    1: humanPolicy,  
    2: minimaxPolicy,
}

state = game.startState()
while not game.isEnd(state):
    player = game.player(state)
    policy = policies[player]
    available_actions = game.actions(state)
    action = policy(game, state)
    state = game.succ(state, action, player)

print('Game over!')
winner = game.utility(state)
print_winner(winner)