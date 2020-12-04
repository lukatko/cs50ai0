"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count_x = 0
    count_o = 0
    for i in board:
        for j in i:
            if (j == X):
                count_x += 1
            elif (j == O):
                count_o += 1
    if (count_x <= count_o):
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                all_actions.add((i, j))
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in (O, X):
        for j in range(3):
            if (board[j][0] == i and board[j][1] == i and board[j][2] == i):
                return i
            if (board[0][j] == i and board[1][j] == i and board[2][j] == i):
                return i
        if (board[0][0] == i and board[1][1] == i and board[2][2] == i):
            return i
        if (board[2][0] == i and board[1][1] == i and board[0][2] == i):
            return i
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in (O, X):
        for j in range(3):
            if (board[j][0] == i and board[j][1] == i and board[j][2] == i):
                return True
            if (board[0][j] == i and board[1][j] == i and board[2][j] == i):
                return True
        if (board[0][0] == i and board[1][1] == i and board[2][2] == i):
            return True
        if (board[2][0] == i and board[1][1] == i and board[0][2] == i):
            return True
    for i in board:
        for j in i:
            if (j == EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winners = winner(board)
    if (X == winners):
        return 1
    elif (O == winners):
        return -1
    return 0

def recursion(board):
    if (terminal(board)):
        return utility(board)
    curr_board = [row[:] for row in board]
    curr_player = player(board)
    all_combinations = []
    for move in actions(board):
        new_board = result(curr_board, move)
        res = recursion(new_board)
        all_combinations.append(res)
        if (curr_player == X and res == 1):
            break
        elif (curr_player == O and res == -1):
            break

    if (curr_player == X):
        return max(all_combinations)
    else:
        return min(all_combinations)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    if (player(board) == X):
        best_so_far = -2
    else:
        best_so_far = 2
    best_move = ()
    for move in actions(board):
        new_board = [row[:] for row in board]
        res = recursion(result(new_board, move))
        if (player(board) == X):
            if (res > best_so_far):
                best_so_far = res
                best_move = move
                if (res == 1):
                    break
        else:
            if (res < best_so_far):
                best_so_far = res
                best_move = move
                if (res == -1):
                    break
    
    return best_move


    
        


