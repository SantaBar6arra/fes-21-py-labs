class Board:
    ROW_LABELS = ["1", "2", "3", "4", "5", "6", "7", "8"]
    COL_LABELS = ["a", "b", "c", "d", "e", "f", "g", "h"]
    EMPTY_SQUARE = " " # змінна, яка зберігає символ порожньої клітинки
    
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, "."],
            [".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE],
            [self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, "."],
            [".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE, ".", self.EMPTY_SQUARE],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        
    def move_piece(self, from_square, to_square):
        from_file, from_rank = from_square
        to_file, to_rank = to_square
        self.board[to_rank][to_file] = self.board[from_rank][from_file]
        self.board[from_rank][from_file] = self.EMPTY_SQUARE

    def display_board(self):
        # Print column labels
        print("  " + " ".join(self.COL_LABELS))
        # Print rows with labels
        for i in range(len(self.board)):
            print(self.ROW_LABELS[i] + " " + " ".join(self.board[i]))

    def is_valid_move(self, from_square, to_square):
        from_file, from_rank = from_square
        to_file, to_rank = to_square
        piece = self.board[from_rank][from_file]
        target = self.board[to_rank][to_file]
        if piece == self.EMPTY_SQUARE:
            return False
        if target != self.EMPTY_SQUARE and target.isupper() == piece.isupper():
            return False
        return True
        
class Piece:
    def __init__(self, color):
        self.color = color


class Pawn(Piece):
    SYMBOL = "P"
    
    def __init__(self, color):
        super().__init__(color)


class Knight(Piece):
    SYMBOL = "N"
    
    def __init__(self, color):
        super().__init__(color)


class Bishop(Piece):
    SYMBOL = "B"
    
    def __init__(self, color):
        super().__init__(color)


class Rook(Piece):
    SYMBOL = "R"
    
    def __init__(self, color):
        super().__init__(color)


class Queen(Piece):
    SYMBOL = "Q"
    
    def __init__(self, color):
        super().__init__(color)


class King(Piece):
    SYMBOL = "K"
    
    def __init__(self, color):
        super().__init__(color)


class PieceFactory:
    def create_piece(self, piece_type, color):
        if piece_type == "Pawn":
            return Pawn(color)
        elif piece_type == "Knight":
            return Knight(color)
        elif piece_type == "Bishop":
            return Bishop(color)
        elif piece_type == "Rook":
            return Rook(color)
        elif piece_type == "Queen":
            return Queen(color)
        elif piece_type == "King":
            return King(color)


class Game:
    def __init__(self):
        self.board = Board()
        self.piece_factory = PieceFactory()

    def start(self):
        self.board.display_board()
        while True:
            move = input("Enter move (e.g. e2e4): ")
            from_square = (ord(move[0]) - 97, int(move[1]) - 1)
            to_square = (ord(move[2]) - 97, int(move[3]) - 1)
            self.board.move_piece(from_square, to_square)
            self.board.display_board()
            # Перевірка чи гра закінчена
            game_over = self.is_game_over()
            if game_over:
               print("Game over!")
               break
    def is_game_over(self):
           return False


if __name__ == "__main__":
    game = Game()
    game.start()