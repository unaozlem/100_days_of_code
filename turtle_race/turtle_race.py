from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet!", prompt = "Who will win the game? Pick a clolor: \n red, orange, yellow, green, blue or purple ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-130, -80, -30, 20, 70, 120]
all_turtles = []

is_race_on = False

for turtle_index in range(0, 6):
   new_turtle = Turtle("turtle")
   new_turtle.penup()
   new_turtle.color(colors[turtle_index])
   new_turtle.goto(x = -230, y = y_positions[turtle_index])
   all_turtles.append(new_turtle)


if user_bet:
   is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(winning_color)
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lose!. The winner is {winning_color}")

        random_distance = random.randint(0,20)
        turtle.forward(random_distance)

   
      
screen.exitonclick()