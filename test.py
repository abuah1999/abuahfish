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

    def assert_right_move(self, fen, depth, rightmove):
        board = Board(fen)
        result = search.searcher(board, depth, 40000000, -1)
        ourmove = result[1]
        self.assertEqual(ourmove.uci(), rightmove)

    def test_knight_fork_1(self):
        fen = "3r1rk1/2p2ppp/p1p5/4P3/3R1n2/2P2P2/P1P2B1P/2K4R b - - 1 22"
        self.assert_right_move(fen, 2, "f4e2")

    def test_knight_fork_2(self):
        fen = "k6r/ppBq2pp/5pb1/3p4/1Q1n2P1/5P2/PP5P/2R1R1K1 b - - 2 25"
        self.assert_right_move(fen, 2, "d4f3")

    def test_knight_fork_3(self):
        fen = "r1r5/3b1k1p/1Q1B2q1/P3p1p1/5p2/3P1NnP/1PP3P1/6KR w - - 0 31"
        self.assert_right_move(fen, 2, "f3e5")

    def test_mate_in_II_1(self):
        fen = "5r2/2pnN1pk/p2p4/1p6/3P4/2P3K1/Pr6/4R3 w - - 0 33"
        self.assert_right_move(fen, 2, "e1h1")

    def test_mate_in_II_2(self):
        fen = "7Q/6p1/8/p3Ppkp/3Pq3/2P4P/1r4PK/8 w - - 0 37"
        self.assert_right_move(fen, 3, "h8g7")

    def test_remove_defender_1(self):
        fen = "rnq1r1k1/pp3pb1/3p2n1/2pP1bB1/2P5/2N3P1/PPQ2PBP/R3R1K1 w - - 5 17"
        self.assert_right_move(fen, 2, "e1e8")

    def test_remove_defender_2(self):
        fen = "r2q1rk1/ppp1b1pp/5p2/3n3b/2QP4/5N1P/PP1N1PP1/R1B1R1K1 w - - 0 15"
        self.assert_right_move(fen, 5, "e1e7")

    def test_queen_fork_1(self):
        fen = "rnbqkbnr/pppp3p/6p1/3Q1p2/8/2N5/PPP1PPPP/R1B1KBNR w KQkq - 0 5"
        self.assert_right_move(fen, 3, "d5e5")

    def test_discovered_attack_1(self):
        fen = "3r2k1/pb2bppp/1p2pn2/3qN3/8/1P1BPP2/PB2Q1PP/3R2K1 w - - 3 19"
        self.assert_right_move(fen, 2, "d3h7")

    def test_discovered_attack_2(self):
        fen = "5r2/3k1r1p/p2p1q2/1ppP4/3P4/PP3BQ1/1B2K3/5R2 w - - 1 33"
        self.assert_right_move(fen, 3, "f3g4")

    def test_capture_1(self):
        fen = "r3kbnr/pp1q1pp1/2n4p/2N1p3/Q1Pp4/3P2Pb/PP2PPBP/RNB2RK1 b kq - 0 10"
        self.assert_right_move(fen, 2, "f8c5")

    def test_skewer_1(self):
        fen = "8/7R/1N3p2/8/2b5/2r2k2/7K/8 w - - 0 44"
        self.assert_right_move(fen, 3, "h7h3")


if __name__ == '__main__':
    unittest.main()