from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-210, 240))
            new_car.car_speed = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_cars_speed(self):
        self.move_speed += MOVE_INCREMENT

    def car_collision(self, player):
        player_collided = False
        for car in self.all_cars:
            if player.distance(car) < 20:
                player_collided = True
                break

        return player_collided
