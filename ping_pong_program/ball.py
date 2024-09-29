from turtle import Turtle

# X = 0
# Y = 0


class CreateBall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.direction_x = 10
        self.direction_y = 10
        self.ball_speed = 0.08

    def ball_move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.setpos(new_x, new_y)

    def ball_bounce_y(self):
        self.direction_y *= -1

    def ball_bounce_x(self):
        self.direction_x *= -1
        self.add_ball_speed()

    def reset_ball(self):
        self.setpos(0, 0)
        self.ball_speed = 0.08
        self.ball_bounce_x()

    def add_ball_speed(self):
        self.ball_speed *= 0.8



