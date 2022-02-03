import chess
import random
import search
import time

def main():

    board = chess.Board()

    def output(line):
        print(line)

    stack = []
    while True:
        if stack:
            smove = stack.pop()
        else:
            smove = input()

        if smove == 'quit':
            break

        elif smove == 'uci':
            output('id name Abuahfish')
            output('id author Amaechi Abuah')
            output('uciok')

        elif smove == 'isready':
            output('readyok')

        elif smove == 'ucinewgame':
            board.reset()

        elif smove.startswith('position'):
            params = smove.split(' ')
            idx = smove.find('moves')

            if idx >= 0:
                moveslist = smove[idx:].split()[1:]
            else:
                moveslist = []

            if params[1] == 'fen':
                if idx >= 0:
                    fenpart = smove[:idx]
                else:
                    fenpart = smove

                _, _, fen = fenpart.split(' ', 2)

            elif params[1] == 'startpos':
                fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

            else:
                pass

            board = chess.Board(fen)

            for move in moveslist:
                board.push(chess.Move.from_uci(move))

        elif smove.startswith('go'):
            start_time = time.time()
            #minimaxresult = search.minimax(board, 3, board.turn)
            #ourmove = minimaxresult[1]
            #nodes = minimaxresult[2]
            #alphabetaminimaxresult = search.alphabetaminimax(board, 3, -9999, 9999, board.turn)
            #ourmove = alphabetaminimaxresult[1]
            #nodes = alphabetaminimaxresult[2]
            result = search.searcher(board, 3)
            ourmove = result[1]
            nodes = result[2]
            end_time = time.time()
            time_taken = end_time - start_time
            output('bestmove ' + ourmove.uci())
            output('time taken: ' + str(time_taken))
            output('nodes: ' + str(nodes))
            board.push(ourmove)

        else:
            pass

if __name__ == '__main__':
    main()