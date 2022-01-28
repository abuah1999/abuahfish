import chess
import random 

def main():

    board = chess.Board()

    def output(line):
        print(line)

    def selectmove():
        return random.choice(list(board.legal_moves))

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
            output('bestmove ' + selectmove().uci())
            board.push(selectmove())

        else:
            pass

if __name__ == '__main__':
    main()