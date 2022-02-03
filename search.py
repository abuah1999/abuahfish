import evaluate
import random
import time

MVV_LVA = [
    [0, 0, 0, 0, 0, 0, 0],       # victim None, attacker None, P, N, B, R, Q, K
    [0, 15, 14, 13, 12, 11, 10], # victim P, attacker None, P, N, B, R, Q, K
    [0, 25, 24, 23, 22, 21, 20], # victim N, attacker None, P, N, B, R, Q, K
    [0, 35, 34, 33, 32, 31, 30], # victim B, attacker None, P, N, B, R, Q, K
    [0, 45, 44, 43, 42, 41, 40], # victim R, attacker None, P, N, B, R, Q, K
    [0, 55, 54, 53, 52, 51, 50], # victim Q, attacker None, P, N, B, R, Q, K
    [0, 0, 0, 0, 0, 0, 0],       # victim K, attacker None, P, N, B, R, Q, K
]

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]

def scoreMoves(moves, board):
    move_scores = {}
    for move in moves:
        capturing_piece = board.piece_at(move.from_square)
        captured_piece = board.piece_at(move.to_square)
        if (capturing_piece and captured_piece):   
            move_scores[move] = MVV_LVA[captured_piece.piece_type][capturing_piece.piece_type]
        else:
            move_scores[move] = 0
    return move_scores

def pickMove(moves, move_scores, start_index):
    for i in range(start_index+1, len(moves)):
        if (move_scores[moves[i]] > move_scores[moves[start_index]]):
            swap(moves, start_index, i)

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

    # move ordering stuff goes here
    moves = list(board.legal_moves)
    move_scores = scoreMoves(moves, board)

    for i in range(len(moves)):
        #pickMove
        pickMove(moves, move_scores, i)
        current_move = moves[i]
        board.push(current_move)
        alphabetaminimaxresult = alphabetaminimax(board, depth-1, alpha, beta, nextPlayer)
        eval = alphabetaminimaxresult[0]
        nodes += alphabetaminimaxresult[2]
        board.pop()
        maxEval = max(maxEval, eval)
        minEval = min(minEval, eval)
        if (maximizingPlayer):
            if (eval == maxEval):
                bestmove = current_move   
            alpha = max(alpha, eval)
        else:
            if (eval == minEval):
                bestmove = current_move   
            beta = min(beta, eval)
        if (beta < alpha):
            #print('player at cuttoff: white') if maximizingPlayer else print('player at cuttoff: black')
            break
    if (maximizingPlayer):
        return([maxEval, bestmove, nodes+1])
    else:
        return([minEval, bestmove, nodes+1])

def searcher(board, depth, our_time, movetime):
    moves_remain = 40
    start_time = time.time()
    for i in range(1, depth+1):
        result = alphabetaminimax(board, i, -9999, 9999, board.turn)
        if (i == depth or
            #or if move time is up
            (movetime > 0 and (time.time() - start_time) * 1000 > movetime) or
            ((time.time() - start_time) * 1000 > our_time/moves_remain)):
            return result


