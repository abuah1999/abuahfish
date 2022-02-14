import evaluate
#import random
from time import time
import quiet

MVV_LVA = [
    [0, 0, 0, 0, 0, 0, 0],       # victim None, attacker None, P, N, B, R, Q, K
    [0, 15, 14, 13, 12, 11, 10], # victim P, attacker None, P, N, B, R, Q, K
    [0, 25, 24, 23, 22, 21, 20], # victim N, attacker None, P, N, B, R, Q, K
    [0, 35, 34, 33, 32, 31, 30], # victim B, attacker None, P, N, B, R, Q, K
    [0, 45, 44, 43, 42, 41, 40], # victim R, attacker None, P, N, B, R, Q, K
    [0, 55, 54, 53, 52, 51, 50], # victim Q, attacker None, P, N, B, R, Q, K
    [0, 0, 0, 0, 0, 0, 0],       # victim K, attacker None, P, N, B, R, Q, K
]

MOVES_REMAIN = 40


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
def alphabetaminimax(board, start_depth, depth, alpha, beta, maximizingPlayer, st, ot, mt):

    if ((mt > 0 and (time() - st) * 1000 > mt) or
            ((time() - st) * 1000 > ot/MOVES_REMAIN)):
        while(start_depth > depth):
            board.pop()
            depth += 1   
        raise Exception("time up")

    if (maximizingPlayer):
        nextPlayer = False
    else:
        nextPlayer = True

    if (board.is_game_over() or depth == 0):
        return([evaluate.evaluate_board(board), None, 1])

    #if (depth == 0):
    #    return([quiet.quietsearch(board, 1, -9999, 9999, nextPlayer), None, 1])
    
    maxEval = -9999
    minEval = 9999
    nodes = 0
    #bestmove = random.choice(list(board.legal_moves))

    # move ordering stuff goes here
    moves = list(board.legal_moves)
    move_scores = scoreMoves(moves, board)

    for i in range(len(moves)):
        #pickMove
        pickMove(moves, move_scores, i)
        current_move = moves[i]
        board.push(current_move)
        alphabetaminimaxresult = alphabetaminimax(board, start_depth, depth-1, alpha, beta, nextPlayer, st, ot, mt)
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
            break
    if (maximizingPlayer):
        return([maxEval, bestmove, nodes+1])
    else:
        return([minEval, bestmove, nodes+1])

def searcher(board, depth, our_time, movetime):
    start_time = time()
    result = alphabetaminimax(board, 0, 0, -9999, 9999, board.turn, start_time, our_time, movetime)
    for i in range(1, depth+1):
        try:
            result = alphabetaminimax(board, i, i, -9999, 9999, board.turn, start_time, our_time, movetime)
        except:
            return result
        if (i == depth or
            #or if move time is up
            (movetime > 0 and (time() - start_time) * 1000 > movetime) or
            ((time() - start_time) * 1000 > our_time/MOVES_REMAIN)):
            return result


