import evaluate
import random

"""def moveOrder(moves, moveScoreList):
    movesWithScores = []
    sortedMoves = []
    for i in range(len(moves)):
        movesWithScores.append([moveScoreList[i], moves[i]])"""

MVV_LVA = [
    [0, 0, 0, 0, 0, 0, 0],       # victim None, attacker None, P, N, B, R, Q, K
    [0, 15, 14, 13, 12, 11, 10], # victim P, attacker None, P, N, B, R, Q, K
    [0, 25, 24, 23, 22, 21, 20], # victim N, attacker None, P, N, B, R, Q, K
    [0, 35, 34, 33, 32, 31, 30], # victim B, attacker None, P, N, B, R, Q, K
    [0, 45, 44, 43, 42, 41, 40], # victim R, attacker None, P, N, B, R, Q, K
    [0, 55, 54, 53, 52, 51, 50], # victim Q, attacker None, P, N, B, R, Q, K
    [0, 0, 0, 0, 0, 0, 0],       # victim K, attacker None, P, N, B, R, Q, K
]


# returns evaluation
def alphabetaminimax(board, depth, alpha, beta, maximizingPlayer):
    if (depth == 0 or board.is_game_over()):
        return([evaluate.evaluate_board(board), None, 1])
    
    maxEval = -9999
    minEval = 9999
    nodes = 0
    bestmove = random.choice(list(board.legal_moves))

    if (maximizingPlayer):
        nextPlayer = False
    else:
        nextPlayer = True

    for move in board.legal_moves:
        board.push(move)
        alphabetaminimaxresult = alphabetaminimax(board, depth-1, alpha, beta, nextPlayer)
        eval = alphabetaminimaxresult[0]
        nodes += alphabetaminimaxresult[2]
        board.pop()
        maxEval = max(maxEval, eval)
        minEval = min(minEval, eval)
        if (maximizingPlayer):
            if (eval == maxEval):
                bestmove = move   
            alpha = max(alpha, eval)
        else:
            if (eval == minEval):
                bestmove = move   
            beta = min(beta, eval)
        if (beta < alpha):
            #print('player at cuttoff: white') if maximizingPlayer else print('player at cuttoff: black')
            break
    if (maximizingPlayer):
        return([maxEval, bestmove, nodes+1])
    else:
        return([minEval, bestmove, nodes+1])

def searcher(board, depth):
    for i in range(1, depth+1):
        result = alphabetaminimax(board, i, -9999, 9999, board.turn)
        if (i == depth):
            #or if move time is up
            return result



    """if (maximizingPlayer):
        maxEval = -9999
        nodes = 0
        #bestmove = random.choice(list(board.legal_moves))
        for move in board.legal_moves:
            board.push(move)
            alphabetaminimaxresult = alphabetaminimax(board, depth-1, alpha, beta, False)
            eval = alphabetaminimaxresult[0]
            nodes += alphabetaminimaxresult[2]
            board.pop()
            maxEval = max(maxEval, eval)
            if (eval == maxEval):
                bestmove = move   
            alpha = max(alpha, eval)
            if (beta <= alpha):
                break
             
        return([maxEval, bestmove, nodes+1])
    
    else:
        minEval = 9999
        nodes = 0
        #bestmove = random.choice(list(board.legal_moves))
        for move in board.legal_moves:
            board.push(move)
            alphabetaminimaxresult = alphabetaminimax(board, depth-1, alpha, beta, True)
            eval = alphabetaminimaxresult[0]
            nodes += alphabetaminimaxresult[2]
            board.pop()
            minEval = min(minEval, eval)
            if (eval == minEval):
                bestmove = move
            beta = min(beta, eval)
            if (beta <= alpha):
                break
            
        return([minEval, bestmove, nodes+1])"""

# returns best move
"""def searcher(board, depth):
    # progressive deepening


    for i in range(depth):
        if (board.turn):
            maxEval = -9999
            for move in board.legal_moves:
                board.push(move)
                eval = alphabetaminimax(board, i, -9999, 9999, False)
                board.pop()
                maxEval = max(maxEval, eval)
                if (eval == maxEval):
                    bestmove = move
        else:
            minEval = 9999
            for move in board.legal_moves:
                board.push(move)
                eval = alphabetaminimax(board, i, -9999, 9999, True)
                board.pop()
                minEval = min(minEval, eval)
                if (eval == minEval):
                    bestmove = move
        if (i == depth - 1):
            # or if time for move is up (to be added later)
            return bestmove
        else:
            pass
 """           



def minimax(board, depth, maximizingPlayer):
    if (depth == 0 or board.is_game_over()):
        return([evaluate.evaluate_board(board), None, 1])

    if (maximizingPlayer):
        maxEval = -9999
        nodes = 0
        for move in board.legal_moves:
            board.push(move)
            minimaxresult = minimax(board, depth-1, False)
            eval = minimaxresult[0]
            nodes += minimaxresult[2]
            maxEval = max(maxEval, eval)
            if (eval == maxEval):
                bestmove = move
            board.pop()
        return([maxEval, bestmove, nodes+1])
    
    else:
        minEval = 9999
        nodes = 0
        for move in board.legal_moves:
            board.push(move)
            minimaxresult = minimax(board, depth-1, True)
            eval = minimaxresult[0]
            nodes += minimaxresult[2]
            minEval = min(minEval, eval)
            if (eval == minEval):
                bestmove = move
            board.pop()
        return([minEval, bestmove, nodes+1])

