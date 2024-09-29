from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, screen, x, y):
        super().__init__()
        self.shape('square')
        self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1) # 기본 크기가 20 * 20임
        self.goto(x, y)
        self.color('white')
        self.penup()

        if x > 0:
            screen.listen()
            screen.onkey(self.up, key='Up')
            screen.onkey(self.down, key='Down')
        elif x < 0:
            screen.listen()
            screen.onkey(self.up, key='w')
            screen.onkey(self.down, key='s')

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)



