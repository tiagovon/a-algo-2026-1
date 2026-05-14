"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X sempre começa, então enquanto houver tantos X quanto O (ou zero), é a vez de X
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Levanta exceção se a ação for inválida
    if i not in range(3) or j not in range(3):
        raise Exception("Ação fora do tabuleiro")
    if board[i][j] != EMPTY:
        raise Exception("Célula já ocupada")

    # Deep copy pra não modificar o tabuleiro original (importante pro minimax)
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Linhas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Colunas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Alguém ganhou
    if winner(board) is not None:
        return True

    # Ainda há células vazias -> jogo continua
    for row in board:
        if EMPTY in row:
            return False

    # Tabuleiro cheio sem vencedor -> empate (jogo acabou)
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        # X maximiza
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = _min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
                if best_value == 1:
                    # Já achou o melhor possível, não precisa procurar mais
                    return best_action
        return best_action
    else:
        # O minimiza
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = _max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
                if best_value == -1:
                    return best_action
        return best_action


def _max_value(board):
    """
    Auxiliar do minimax: retorna o maior valor de utilidade
    que o jogador maximizador (X) consegue garantir a partir deste tabuleiro.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, _min_value(result(board, action)))
        if v == 1:
            return v  # poda: não dá pra fazer melhor que 1
    return v


def _min_value(board):
    """
    Auxiliar do minimax: retorna o menor valor de utilidade
    que o jogador minimizador (O) consegue garantir a partir deste tabuleiro.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, _max_value(result(board, action)))
        if v == -1:
            return v  # poda: não dá pra fazer pior que -1
    return v