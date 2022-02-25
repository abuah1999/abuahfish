from chess import Board
import search
import evaluate 
import unittest

class TestChess(unittest.TestCase):
    def test_eval_black_checkmated(self):
        board = Board("rnbqkbnr/ppppp2p/5p2/6pQ/3PP3/8/PPP2PPP/RNB1KBNR b KQkq - 1 3")
        self.assertEqual(evaluate.evaluate_board(board), 9999)

    def test_eval_white_checkmated(self):
        board = Board("rnb1kbnr/pppp1ppp/4p3/8/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3")
        self.assertEqual(evaluate.evaluate_board(board), -9999)

    def test_eval_black_Queen_up(self):
        board = Board("rnbqkb1r/pppp1ppp/8/4p2n/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 4")
        self.assertLess(evaluate.evaluate_board(board), 0)

    def test_eval_white_Queen_up(self):
        board = Board("r1bBkbnr/pppp1ppp/8/4p3/3nP3/3P4/PPP2PPP/RN1QKBNR b KQkq - 0 4")
        self.assertGreater(evaluate.evaluate_board(board), 0)

    def test_eval_white_better_development(self):
        board = Board("rnbqkbnr/ppppp1pp/4Pp2/3P4/2B2B2/2NQ1N2/PPP2PPP/3RR1K1 w - - 1 14")
        self.assertGreater(evaluate.evaluate_board(board), 0)

    def test_eval_black_better_development(self):
        board = Board("3rr1k1/ppp2ppp/2nq1n2/2bppb2/8/5P2/PPPPP1PP/RNBQKBNR b - - 17 11")
        self.assertLess(evaluate.evaluate_board(board), 0)

    def test_eval_white_poor_king(self):
        board = Board("rnbqkbnr/pppppppp/8/4K3/8/8/PPPPPPPP/RNBQ1BNR w kq - 0 1")
        self.assertLess(evaluate.evaluate_board(board), 0)

    def test_eval_black_poor_king(self):
        board = Board("rnbq1bnr/pppppppp/8/8/4k3/8/PPPPPPPP/RNBQKBNR w KQ - 0 1")
        self.assertGreater(evaluate.evaluate_board(board), 0)


if __name__ == '__main__':
    unittest.main()