import evaluate


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
    capture_moves = []
    move_scores = {}
    for move in moves:
        capturing_piece = board.piece_at(move.from_square)
        captured_piece = board.piece_at(move.to_square)  
        if (capturing_piece and captured_piece):   
            capture_moves.append(move)
            move_scores[move] = MVV_LVA[captured_piece.piece_type][capturing_piece.piece_type]
        else:
            pass
    return [capture_moves, move_scores]

"""def scoreMoves(moves, board):
    move_scores = {}
    for move in moves:
        capturing_piece = board.piece_at(move.from_square)
        captured_piece = board.piece_at(move.to_square)
        if (capturing_piece and captured_piece):   
            move_scores[move] = MVV_LVA[captured_piece.piece_type][capturing_piece.piece_type]
        else:
            move_scores[move] = 0
    return move_scores"""

def pickMove(moves, move_scores, start_index):
    for i in range(start_index+1, len(moves)):
        if (move_scores[moves[i]] > move_scores[moves[start_index]]):
            swap(moves, start_index, i)

# returns evaluation
def search(board, depth, alpha, beta, maximizingPlayer):
    #if (depth == 0 or board.is_game_over()):
    #    return([evaluate.evaluate_board(board), None, 1])
    
    maxEval = -9999
    minEval = 9999
    #bestmove = random.choice(list(board.legal_moves))

    if (maximizingPlayer):
        nextPlayer = False
    else:
        nextPlayer = True

    # move ordering stuff goes here
    moves = list(board.legal_moves)
    capture_moves_with_scores = scoreMoves(moves, board)
    capture_moves = capture_moves_with_scores[0]
    move_scores = capture_moves_with_scores[1]

    if(depth == 0 or len(capture_moves) == 0 or board.is_game_over()):
        return evaluate.evaluate_board(board)

    for i in range(len(capture_moves)):
        #pickMove
        pickMove(capture_moves, move_scores, i)
        current_move = capture_moves[i]
        board.push(current_move)
        eval = search(board, depth-1, alpha, beta, nextPlayer)
        board.pop()
        maxEval = max(maxEval, eval)
        minEval = min(minEval, eval)
        if (maximizingPlayer):   
            alpha = max(alpha, eval)
        else:   
            beta = min(beta, eval)
        if (beta < alpha):
            break
    if (maximizingPlayer):
        return(maxEval)
    else:
        return(minEval)


