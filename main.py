from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    new_turtle.color(colors[i])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"{user_bet} is Winner. You Win!")
                screen.bgcolor("LimeGreen")
            else:
                print(f"{turtle.pencolor()} is Winner.You Lost!")
                screen.bgcolor("Tomato")


screen.exitonclick()


