from turtle import Turtle, Screen
from paddle import Paddle
from ball import CreateBall
import time
from scoreboard import ScoreBoard

turtle = Turtle()
screen = Screen()

screen.title('Pong')
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_r = Paddle(screen, 350, 0)
paddle_l = Paddle(screen, -350, 0)
ball = CreateBall()

score_board = ScoreBoard()

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(ball.ball_speed)
  ball.ball_move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.ball_bounce_y()

  if ball.distance(paddle_r) < 70 and ball.xcor() > 320 or ball.distance(
      paddle_l) < 70 and ball.xcor() < -320:
    ball.ball_bounce_x()

  # 오른쪽 패들이 공을 놓친 경우
  if ball.xcor() > 400:
    ball.reset_ball()
    score_board.add_l_score()

  # 왼쪽 패들이 공을 놓친 경우
  if ball.xcor() < -400:
    ball.reset_ball()
    score_board.add_r_score()

  if score_board.l_score >= 5 or score_board.r_score >= 5:
    score_board.game_over()
    game_is_on = False

screen.exitonclick()
