import evaluate

def minimax(board, depth, maximizingPlayer):
    if (depth == 0 or board.is_game_over()):
        return([evaluate.evaluate_board(board), None])

    if (maximizingPlayer):
        maxEval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth-1, False)[0]
            maxEval = max(maxEval, eval)
            if (eval == maxEval):
                bestmove = move
            board.pop()
        return([maxEval, bestmove])
    
    else:
        minEval = 9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth-1, True)[0]
            minEval = min(minEval, eval)
            if (eval == minEval):
                bestmove = move
            board.pop()
        return([minEval, bestmove])

