from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_check()


    def score_check(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 60, 'normal'))
        self.setpos(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 60, 'normal'))

    def add_l_score(self):
        self.l_score += 1
        self.score_check()

    def add_r_score(self):
        self.r_score += 1
        self.score_check()

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 60, 'normal'))

