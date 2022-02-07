from chess import WHITE, BLACK, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, square_mirror 

pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]
rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]


def evaluate_board(board): 
  if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
  if board.is_stalemate():
        return 0
  if board.is_insufficient_material():
        return 0
  wp = len(board.pieces( PAWN,  WHITE))
  bp = len(board.pieces( PAWN,  BLACK))
  wn = len(board.pieces( KNIGHT,  WHITE))
  bn = len(board.pieces( KNIGHT,  BLACK))
  wb = len(board.pieces( BISHOP,  WHITE))
  bb = len(board.pieces( BISHOP,  BLACK))
  wr = len(board.pieces( ROOK,  WHITE))
  br = len(board.pieces( ROOK,  BLACK))
  wq = len(board.pieces( QUEEN,  WHITE))
  bq = len(board.pieces( QUEEN,  BLACK))
  material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
  pawnsq = sum([pawntable[i] for i in board.pieces( PAWN,  WHITE)])
  pawnsq = pawnsq + sum([-pawntable[ square_mirror(i)]
                        for i in board.pieces( PAWN,  BLACK)])
  knightsq = sum([knightstable[i] for i in board.pieces( KNIGHT,  WHITE)])
  knightsq = knightsq + sum([-knightstable[ square_mirror(i)]
                            for i in board.pieces( KNIGHT,  BLACK)])
  bishopsq = sum([bishopstable[i] for i in board.pieces( BISHOP,  WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[ square_mirror(i)]
                            for i in board.pieces( BISHOP,  BLACK)])
  rooksq = sum([rookstable[i] for i in board.pieces( ROOK,  WHITE)])
  rooksq = rooksq + sum([-rookstable[ square_mirror(i)]
                        for i in board.pieces( ROOK,  BLACK)])
  queensq = sum([queenstable[i] for i in board.pieces( QUEEN,  WHITE)])
  queensq = queensq + sum([-queenstable[ square_mirror(i)]
                          for i in board.pieces( QUEEN,  BLACK)])
  kingsq = sum([kingstable[i] for i in board.pieces( KING,  WHITE)])
  kingsq = kingsq + sum([-kingstable[ square_mirror(i)]
                        for i in board.pieces( KING,  BLACK)])
  eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval
  else:
      return eval