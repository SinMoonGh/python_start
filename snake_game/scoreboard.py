from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.screen_score()


    def add_score(self):
        self.score += 1
        self.screen_score()

    def reset(self):
        if self.score > self.high_score:
            # self.high_score = self.score
            self.high_score_data()
        self.score = 0
        self.screen_score()

    def screen_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}",
                   move=False,
                   align=ALIGN,
                   font=FONT)

    # def open_data_read(self):
    #     with open('data.txt', mode='r') as file:
    #         self.high_score = int(file.read())


    def high_score_data(self):
        with open('data.txt', 'w') as file:
            file.write(f'{self.score}')

        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGN, font=FONT)

