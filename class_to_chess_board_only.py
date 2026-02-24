import turtle

class ChessBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.rows = 8
        self.cols = 8
        self.size = 50
        self.draw_board()	

    def get_xy(self, r, c):
        """Convert row, col to screen x, y (centered on screen)"""
        x = -(self.cols * self.size) / 2 + c * self.size
        y = (self.rows * self.size) / 2 - r * self.size
        return x, y

    def draw_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                c = "saddle brown" if (row + col) % 2 == 0 else "bisque"
                self.fillcolor(c)

                x, y = self.get_xy(row, col)
                self.penup()
                self.goto(x, y)
                self.pendown()
                self.begin_fill()
                for _ in range(4):
                    self.fd(self.size)
                    self.rt(90)
                self.end_fill()

board = ChessBoard()
turtle.done()
