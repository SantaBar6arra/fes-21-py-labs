class Piece:
    """A base class for chess pieces."""

    def __init__(self, icon: str):
        self.icon = icon

    def __str__(self) -> str:
        return self.icon


class King(Piece):
    """A class representing the King chess piece."""

    KING = "♔"

    def __init__(self):
        super().__init__(King.KING)


class Queen(Piece):
    """A class representing the Queen chess piece."""

    QUEEN = "♕"

    def __init__(self):
        super().__init__(Queen.QUEEN)


class Rook(Piece):
    """A class representing the Rook chess piece."""

    ROOK = "♖"

    def __init__(self):
        super().__init__(Rook.ROOK)


class Bishop(Piece):
    """A class representing the Bishop chess piece."""

    BISHOP = "♗"

    def __init__(self):
        super().__init__(Bishop.BISHOP)


class Knight(Piece):
    """A class representing the Knight chess piece."""

    KNIGHT = "♘"

    def __init__(self):
        super().__init__(Knight.KNIGHT)


class Pawn(Piece):
    """A class representing the Pawn chess piece."""

    PAWN = "♙"

    def __init__(self):
        super().__init__(Pawn.PAWN)


class PieceFactory:
    """A factory class for creating chess pieces."""

    @staticmethod
    def create_piece(piece_type: str) -> Piece:
        if piece_type == "KING":
            return King()
        elif piece_type == "QUEEN":
            return Queen()
        elif piece_type == "ROOK":
            return Rook()
        elif piece_type == "BISHOP":
            return Bishop()
        elif piece_type == "KNIGHT":
            return Knight()
        elif piece_type == "PAWN":
            return Pawn()
        else:
            raise ValueError(f"Invalid piece type: {piece_type}")


class Board:
    """A class representing a chess board."""

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.board = [[None for _ in range(columns)] for _ in range(rows)]

    def place_piece(self, piece: Piece, row: int, col: int):
        self.board[row][col] = piece

    def __str__(self) -> str:
        border_top_bottom = "+-------" * self.columns + "+\n"
        board_string = border_top_bottom
        for row in self.board:
            for cell in row:
                board_string += "|\t" + (str(cell) + "\t" if cell else "\t")
            board_string += "|\n"
            board_string += border_top_bottom
        return board_string


class Game:
    """A class representing a chess game."""

    def __init__(self):
        self.board = Board(8, 8)
        self.initialize_pieces()

    def initialize_pieces(self):
        """Places the chess pieces on the board in their starting positions."""
        for col in range(8):
            self.board.place_piece(PieceFactory.create_piece("PAWN"), 1, col)
            self.board.place_piece(PieceFactory.create_piece("PAWN"), 6, col)

        pieces = ["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"]
        for col, piece_type in enumerate(pieces):
            self.board.place_piece(PieceFactory.create_piece(piece_type), 0, col)
            self.board.place_piece(PieceFactory.create_piece(piece_type), 7, col)

    def display_board(self):
        """Prints the current state of the chess board."""
        print(self.board)

if __name__ == "__main__":
    game = Game()
    game.display_board()