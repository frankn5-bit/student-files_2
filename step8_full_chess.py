import turtle

class ChessBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.rows = 8
        self.cols = 8
        self.size = 50
        self.selected = None
        self.turn = "white"

        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.setup_pieces()

        self.screen = turtle.Screen()
        self.screen.title("Chess - Full Rules")
        self.screen.bgcolor("gray")
        self.screen.tracer(0)
        self.draw_board()

        self.screen.onclick(self.handle_click)
        self.screen.mainloop()

    def setup_pieces(self):
        back_black = ["♜","♞","♝","♛","♚","♝","♞","♜"]
        back_white = ["♖","♘","♗","♕","♔","♗","♘","♖"]
        for c in range(8):
            self.board[0][c] = ("black", back_black[c])
            self.board[1][c] = ("black", "♟")
            self.board[7][c] = ("white", back_white[c])
            self.board[6][c] = ("white", "♙")

    def get_xy(self, r, c):
        x = -(self.cols * self.size) / 2 + c * self.size
        y = (self.rows * self.size) / 2 - r * self.size
        return x, y

    def get_rc(self, x, y):
        c = int((x + (self.cols * self.size) / 2) // self.size)
        r = int(((self.rows * self.size) / 2 - y) // self.size)
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return r, c
        return None, None

    def draw_board(self):
        self.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                x, y = self.get_xy(row, col)

                if (row, col) == self.selected:
                    color = "yellow"
                elif (row + col) % 2 == 0:
                    color = "saddle brown"
                else:
                    color = "bisque"

                self.fillcolor(color)
                self.penup()
                self.goto(x, y)
                self.pendown()
                self.begin_fill()
                for _ in range(4):
                    self.fd(self.size)
                    self.rt(90)
                self.end_fill()

                piece = self.board[row][col]
                if piece:
                    self.penup()
                    self.goto(x + self.size / 2, y - self.size + 5)
                    self.pencolor("black")
                    self.write(piece[1], align="center",
                              font=("Arial", self.size // 2, "bold"))

        self.penup()
        self.goto(0, -(self.rows * self.size) / 2 - 30)
        self.pencolor("white")
        self.write(f"{self.turn}'s turn", align="center",
                  font=("Arial", 16, "bold"))
        self.screen.update()

    # ---- MOVEMENT RULES ----

    def path_clear(self, r1, c1, r2, c2):
        """Check if path between two squares is clear (for rook/bishop/queen)"""
        dr = 0 if r2 == r1 else (1 if r2 > r1 else -1)
        dc = 0 if c2 == c1 else (1 if c2 > c1 else -1)
        r, c = r1 + dr, c1 + dc
        while (r, c) != (r2, c2):
            if self.board[r][c] is not None:
                return False
            r += dr
            c += dc
        return True

    def is_valid_move(self, r1, c1, r2, c2):
        piece = self.board[r1][c1]
        if piece is None:
            return False

        color, symbol = piece
        target = self.board[r2][c2]
        dr = r2 - r1
        dc = c2 - c1

        if dr == 0 and dc == 0:
            return False
        if target and target[0] == color:
            return False

        # PAWN
        if symbol in ("♙", "♟"):
            direction = -1 if color == "white" else 1
            start_row = 6 if color == "white" else 1
            if dc == 0 and dr == direction and target is None:
                return True
            if dc == 0 and dr == direction * 2 and r1 == start_row:
                if target is None and self.board[r1 + direction][c1] is None:
                    return True
            if abs(dc) == 1 and dr == direction and target is not None:
                return True
            return False

        # ROOK
        if symbol in ("♖", "♜"):
            if dr != 0 and dc != 0:
                return False
            return self.path_clear(r1, c1, r2, c2)

        # KNIGHT
        if symbol in ("♘", "♞"):
            return (abs(dr), abs(dc)) in [(2, 1), (1, 2)]

        # BISHOP
        if symbol in ("♗", "♝"):
            if abs(dr) != abs(dc):
                return False
            return self.path_clear(r1, c1, r2, c2)

        # QUEEN
        if symbol in ("♕", "♛"):
            if dr == 0 or dc == 0 or abs(dr) == abs(dc):
                return self.path_clear(r1, c1, r2, c2)
            return False

        # KING
        if symbol in ("♔", "♚"):
            return abs(dr) <= 1 and abs(dc) <= 1

        return False

    def handle_click(self, x, y):
        r, c = self.get_rc(x, y)
        if r is None:
            return

        if self.selected is None:
            piece = self.board[r][c]
            if piece and piece[0] == self.turn:
                self.selected = (r, c)
        else:
            sr, sc = self.selected
            target = self.board[r][c]

            if target and target[0] == self.turn:
                self.selected = (r, c)          # reselect own piece
            elif self.is_valid_move(sr, sc, r, c):
                piece = self.board[sr][sc]
                # Pawn promotion
                if piece[1] in ("♙", "♟") and r in (0, 7):
                    queen = "♕" if piece[0] == "white" else "♛"
                    self.board[r][c] = (piece[0], queen)
                else:
                    self.board[r][c] = piece
                self.board[sr][sc] = None
                self.turn = "black" if self.turn == "white" else "white"
                self.selected = None
            else:
                self.selected = None            # invalid move, deselect

        self.draw_board()

board = ChessBoard()
