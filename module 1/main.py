class Board:
    def __init__(self):
        self.board = [
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["  ", ".", "  ", ".", "  ", ".", "   ", "."],
            [". ", "  ", ".", "  ", ".", "  ", ".", " "],
            ["  ", ".", "  ", ".", "  ", ".", "   ", "."],
            [".", "   ", ".", "  ", ".", "  ", ".", " "],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        ]
        self.row_labels = ["1|", "2|", "3|", "4|", "5|", "6|", "7|", "8|"]
        self.col_labels = [" a", " b", " c", "d", " e", " f", "g", " h"]

    def move_piece(self, from_square, to_square):
        from_file, from_rank = from_square
        to_file, to_rank = to_square
        self.board[to_rank][to_file] = self.board[from_rank][from_file]
        self.board[from_rank][from_file] = " "

    def display_board(self):
        # Print column labels
        print("  " + " ".join(self.col_labels))
        # Print rows with labels
        for i in range(len(self.board)):
            print(self.row_labels[i] + " " + " ".join(self.board[i]))


class Piece:
    def __init__(self, color):
        self.color = color


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♙"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♘"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♗"


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♖"


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♕"


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♔"


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
            move = input("Enter move (e.g. b2b4): ")
            from_square = (ord(move[0]) - 97, int(move[1]) - 1)
            to_square = (ord(move[2]) - 97, int(move[3]) - 1)
            self.board.move_piece(from_square, to_square)
            self.board.display_board()


if __name__ == "__main__":
    game = Game()
    game.start()