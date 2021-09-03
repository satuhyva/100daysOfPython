from turtle import Turtle
import random

DISTANCE = 2.5
CAR_COLORS = ["cornflower blue", "light steel blue", "royal blue", "powder blue", "steel blue",
              "light sky blue", "deep sky blue", "light blue", "cadet blue", "sky blue"]
CAR_Y_VALUES = [240, 200, 160, 120, 80, 40, 0, -40, -80, -120, -160, -200, -240]


class CarManager:

    def __init__(self):
        self.cars = self.create_cars()


    @staticmethod
    def create_cars():
        cars = []
        for index in range(0, len(CAR_Y_VALUES)):
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=3)
            color_number = random.randint(0, 9)
            car.color(CAR_COLORS[color_number])
            car.penup()
            random_x = random.randint(-36, 36)
            car.setx(random_x * 10)
            car.sety(CAR_Y_VALUES[index])
            random_direction = random.randint(0, 1)
            if random_direction == 0:
                car.left(180)
            cars.append(car)
        return cars

    def reset_cars(self):
        for index in range(0, len(self.cars)):
            random_x = random.randint(-36, 36)
            self.cars[index].setx(random_x * 10)
            self.cars[index].sety(CAR_Y_VALUES[index])
            random_direction = random.randint(0, 1)
            if random_direction == 0:
                self.cars[index].left(180)

    def move_cars(self):
        for car in self.cars:
            car.forward(DISTANCE)

    def return_cars(self):
        for car in self.cars:
            pos_x = car.xcor()
            if pos_x > 400:
                car.setx(-400)
            if pos_x < -400:
                car.setx(400)

    def detect_hits(self, player):
        hit = False
        for car in self.cars:
            y_car = car.ycor()
            y_player = player.ycor()
            if not (y_car + 10 < y_player - 8 or y_car - 10 > y_player + 15):
                x_car = car.xcor()
                x_player = player.xcor()
                if x_car - 32.5 < x_player - 10 < x_car + 35 or x_car - 32.5 < x_player + 10 < x_car + 32.5:
                    hit = True
        return hit


