import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tourtoise = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()

screen.onkey(fun=tourtoise.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(tourtoise) < 20:
            game_is_on = False
            score.game_over()

    # Detect when player reached finish line
    if tourtoise.ycor() > 260:
        tourtoise.go_to_start()
        car_manager.level_up()
        score.increase_score()



screen.exitonclick()
