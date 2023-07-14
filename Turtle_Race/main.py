from turtle import Turtle,Screen
import random

is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_pos = [-150,-100,-50,50,100,150]
screen = Screen()
all_turtles = []
screen.setup(500, 400)
user_bet = screen.textinput("make youre bet", "what color turtle do you think will win.red, blue, green, yellow,orange, purple")
for turtle_index in range(0,6):
    tim = Turtle("turtle")
    tim.penup()
    tim.goto(-230,y_pos[turtle_index])  
    tim.color(colors[turtle_index]) 
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                result = screen.textinput("Results", f"you won! the winning color is {winning_color} how do you feel")
                break
            else:
                result = screen.textinput("Results", f"you lost! the winning color is {winning_color} how do you feel")
                break

    
screen.exitonclick()
