import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
# screen.screensize(700,700)
screen.tracer(0)
 
racer = Player()
cars  = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(fun = racer.move, key = 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.movecar()
    

    # detect collisio with car
    for i in cars.all_cars:
        if i.distance(racer) < 20:
            level.game_over()
            game_is_on = False

    # detect success
    if racer.finish_line():
        cars.level_up()
        level.increase_level_score()

        

        


screen.mainloop()