import time,sched
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Commands
screen.onkey(fun=player.move, key="w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Turtle arrived at finish line
    if player.ycor() == player.goal:
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_cars_speed()

    # Detect car collision
    if car_manager.car_collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
