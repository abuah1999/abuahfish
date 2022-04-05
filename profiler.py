import cProfile
import search
from chess import Board

board = Board("3r1rk1/2p2ppp/p1p5/4P3/3R1n2/2P2P2/P1P2B1P/2K4R b - - 1 22")

cProfile.run('search.searcher(board, 5, 40000000, -1)')