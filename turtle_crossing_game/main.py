import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
screen.onkey(player.move, "Up")
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    
    car_manager.create_car()
    car_manager.move_cars()

    #Detect car collisions
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Did turtle croosed the street
    if player.is_crossed():
        player.start_over()
        car_manager.next_level()
        scoreboard.update_scoreboard()



        
        

        
screen.exitonclick()