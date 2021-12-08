from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 20
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_COORDINATES:
            self.add_seg(pos)

    def add_seg(self, pos):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.setpos(pos)
        self.snake.append(new_seg)

    def grow(self):
        self.add_seg(self.snake[-1].pos())

    def move_snake(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i-1].pos())
        self.head.forward(SPEED)

    def reset(self):
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
