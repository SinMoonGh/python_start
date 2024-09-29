# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

scoreboard = ScoreBoard()
food = Food()
screen = Screen()

# back_ground
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('well come to snake game!!')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# game_animation
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # 먹이 생성
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # 벽에 부딪히면 사망
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        snake.reset()
        scoreboard.reset()

    # 꼬리 감지
    # 꼬리의 어느 부분이라도 부딪히면 사망임.
    for segment in snake.segments[1:]:
        if segment == snake.snake_head:
            # game_is_on = False
            # scoreboard.game_over()
            pass
        elif snake.snake_head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()