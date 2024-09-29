from turtle import Screen, Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# class snake_bodices:
#     def __init__(self, position):
#         turtle = Turtle()
#         turtle.shape('square')
#         turtle.color('white')
#         turtle.goto(position)
#         # turtle.resizemode('user')
#         # turtle.turtlesize(stretch_wid=1, stretch_len=1)


class Snake:

  def __init__(self):
    self.segments = []
    # screen.delay(80)
    self.snake_body()
    self.snake_head = self.segments[0]

  def snake_body(self):
    for position in STARTING_POSITION:
      self.add_body(position)

  def add_body(self, position):
    new_snake_body = Turtle()
    new_snake_body.shape('square')
    new_snake_body.color('white')
    new_snake_body.penup()
    new_snake_body.goto(position)
    self.segments.append(new_snake_body)

  def extend(self):
    self.add_body(self.segments[-1].position())

  def snake_move(self):
    # 1, 2, 3이 있다고 한다면 3은 2를 쫓아가고, 2는 1을 쫓아가고, 1은 방향을 정한다.
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)

    self.snake_head.forward(MOVE_DISTANCE)

  def up(self):
    if self.snake_head.heading() != DOWN:
      self.snake_head.setheading(UP)

  def down(self):
    if self.snake_head.heading() != UP:
      self.snake_head.setheading(DOWN)

  def left(self):
    if self.snake_head.heading() != RIGHT:
      self.snake_head.setheading(LEFT)

  def right(self):
    if self.snake_head.heading() != LEFT:
      self.snake_head.setheading(RIGHT)

  def reset(self):
    for seg in self.segments:
      seg.goto(1000, 1000)
    self.segments.clear()
    self.snake_body()
    self.snake_head = self.segments[0]
