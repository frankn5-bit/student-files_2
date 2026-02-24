import turtle

class Grid:
    def __init__(self, rows=8, cols=8, size=60):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.selected = None  # tracks clicked piece
        self.turn = "white"   # white goes first

        # Board: None = empty, tuple = (color, symbol)
        self.board = [[None for _ in range(cols)] for _ in range(rows)]
        self.setup_pieces()

        # Turtle setup
        self.screen = turtle.Screen()
        self.screen.title("Chess - Layer 1")
        self.screen.bgcolor("gray")
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.screen.tracer(0)  # instant drawing

        self.draw_board()
        self.screen.onclick(self.handle_click)
        self.screen.mainloop()

    def setup_pieces(self):
        # Black pieces (top)
        back = ["♜","♞","♝","♛","♚","♝","♞","♜"]
        for c in range(8):
            self.board[0][c] = ("black", back[c])
            self.board[1][c] = ("black", "♟")
        # White pieces (bottom)
        back = ["♖","♘","♗","♕","♔","♗","♘","♖"]
        for c in range(8):
            self.board[7][c] = ("white", back[c])
            self.board[6][c] = ("white", "♙")

    def get_xy(self, r, c):
        """Convert row,col to turtle x,y"""
        x = -(self.cols * self.size) / 2 + c * self.size
        y = (self.rows * self.size) / 2 - r * self.size
        return x, y

    def get_rc(self, x, y):
        """Convert turtle x,y to row,col"""
        c = int((x + (self.cols * self.size) / 2) // self.size)
        r = int(((self.rows * self.size) / 2 - y) // self.size)
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return r, c
        return None, None

    def draw_board(self):
        self.t.clear()
        for r in range(self.rows):
            for c in range(self.cols):
                x, y = self.get_xy(r, c)

                # Draw square
                if (r, c) == self.selected:
                    color = "yellow"
                elif (r + c) % 2 == 0:
                    color = "saddle brown"
                else:
                    color = "bisque"

                self.t.penup()
                self.t.goto(x, y)
                self.t.pendown()
                self.t.fillcolor(color)
                self.t.begin_fill()
                for _ in range(4):
                    self.t.forward(self.size)
                    self.t.right(90)
                self.t.end_fill()

                # Draw piece
                piece = self.board[r][c]
                if piece:
                    self.t.penup()
                    self.t.goto(x + self.size/2, y - self.size + 5)
                    self.t.pencolor("black")
                    self.t.write(piece[1], align="center",
                                font=("Arial", self.size//2, "bold"))

        # Turn indicator
        self.t.penup()
        self.t.goto(0, -(self.rows * self.size) / 2 - 30)
        self.t.pencolor("white")
        self.t.write(f"{self.turn}'s turn", align="center",
                    font=("Arial", 16, "bold"))
        self.screen.update()

    def handle_click(self, x, y):
        r, c = self.get_rc(x, y)
        if r is None:
            return

        if self.selected is None:
            # First click: select a piece
            piece = self.board[r][c]
            if piece and piece[0] == self.turn:
                self.selected = (r, c)
        else:
            # Second click: move piece
            sr, sc = self.selected
            target = self.board[r][c]

            # Can't capture your own piece
            if target and target[0] == self.turn:
                self.selected = (r, c)  # reselect
            else:
                # Move it!
                self.board[r][c] = self.board[sr][sc]
                self.board[sr][sc] = None
                self.turn = "black" if self.turn == "white" else "white"
                self.selected = None

        self.draw_board()

chess = Grid()