from turtle import Turtle

# setting snake at center with three square boxes ,capital letter represent it is constant
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# distance for moving the snake
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# crating a class Snake
class SnakeTurtle:

    # constructor of Snake class
    def __init__(self):
        # list to make a snake
        self.snake_maker = []
        # it's a function to create a snake add snake segment in it
        self.create_snake()

        # it is equal to head of the snake at 0 position
        self.head = self.snake_maker[0]

    def create_snake(self):
        # creating an snake
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    # making of snake in add_segment function
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_maker.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_maker[-1].pos())

    def move(self):
        for i in range(len(self.snake_maker) - 1, 0, -1):
            new_x = self.snake_maker[i - 1].xcor()
            new_y = self.snake_maker[i - 1].ycor()
            self.snake_maker[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #  .heading() return the current turtle heading location
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
