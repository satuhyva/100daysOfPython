from turtle import Turtle

DISTANCE = 20
START_POSITIONS = [(0, 0), (-DISTANCE, 0), (-DISTANCE * 2, 0),
                   # (-DISTANCE * 3, 0),  (-DISTANCE * 4, 0),  (-DISTANCE * 5, 0),  (-DISTANCE * 6, 0)
                   ]


class Snake:

    def __init__(self):
        self.snake_bits = []
        self.create_snake(self)

    def add_bit(self, position):
        bit = Turtle(shape="square")
        bit.color("white")
        bit.penup()
        bit.setx(position[0])
        bit.sety(position[1])
        self.snake_bits.append(bit)

    @staticmethod
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_bit(position)

    def move(self):
        for index in range(len(self.snake_bits) - 1, 0, -1):
            one_in_front_x = self.snake_bits[index - 1].xcor()
            one_in_front_y = self.snake_bits[index - 1].ycor()
            self.snake_bits[index].goto(one_in_front_x, one_in_front_y)
        self.snake_bits[0].forward(DISTANCE)

    def up(self):
        if not self.snake_bits[0].heading() == -90 and not self.snake_bits[0].heading() == 270:
            self.snake_bits[0].setheading(90)

    def down(self):
        if not self.snake_bits[0].heading() == 90:
            self.snake_bits[0].setheading(-90)

    def left(self):
        if not self.snake_bits[0].heading() == 0:
            self.snake_bits[0].setheading(180)

    def right(self):
        if not self.snake_bits[0].heading() == 180:
            self.snake_bits[0].setheading(0)

    def grow(self):
        x = self.snake_bits[-1].xcor()
        y = self.snake_bits[-1].ycor()
        self.add_bit((x, y))
