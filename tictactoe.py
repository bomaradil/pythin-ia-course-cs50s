"""
Tic Tac Toe Player
"""

import math, copy, random

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
    if board == initial_state():
        P = X
    else:
        count_X = len([i for i in board if i.count(X) != 0])
        count_O = len([i for i in board if i.count(O) != 0])
        if count_O > count_X:
            P = X
        else:
            P = O
    return P

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    i = 0
    for row in board:
        action.extend([(i, e) for e, cell in enumerate(row) if cell == EMPTY])
        i += 1
    return [a for a in action if len(a) != 0]

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if  new_board[action[0]][action[1]] != EMPTY:
        raise Exception('cell full')
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner_cells():
    """
    Returns the winner cell of the game
    """
    cell = range(3)
    cells = [[(x, y) for y in cell] for x in cell]
    cells.append([(i, i) for i in cell])
    cells.append([(i, 2-i)for i in cell])
    return cells

def winner(board):
    """
    Returns the winner cell of the game, if there is one.
    """
    full_cells = [[board[y[0]][y[1]] for y in x if board[y[0]][y[1]] != EMPTY] for x in winner_cells()]
    full_cells = [i for i in full_cells if len(i) == 3]
    winner = [i[0] for i in full_cells if i[0] == i[1] == i[2]]
    if len(winner) != 0:
        return winner[0]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game = len([x for y in board for x in y if x == EMPTY])
    return game == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    v = []
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v.append(result(board, action))
    lo = hi = EMPTY 
    for val in v:
        if val is EMPTY or val < lo:
            lo = val
        elif  val is EMPTY or val > hi:
            hi = val
    return (lo, hi)
    



def max_value(board):
    v = -math.inf
    max_values = []
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        (v, action)
    return v

def min_value(board):
    v = math.inf
    min_values = []
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        #print((v, action))
    return v
