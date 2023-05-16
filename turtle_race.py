import random
import tkinter.messagebox
from turtle import Turtle, Screen

# making an object of Screen class
screen = Screen()

# changing the tile of screen
screen.title("Turtle races")

# screen height and width
screen.setup(width=500, height=500)

# creating list of colors and players and Y_angle

colors = ["red", "green", "blue", "orange", "yellow"]
players = []
y_angle = [60, 30, 0, -30, -60]


# create_players() is used to create a project
def create_players():
    for j in range(0, 5):
        q = Turtle(shape="turtle")
        q.penup()
        q.color(colors[j])
        q.goto(x=-230, y=y_angle[j])
        players.append(q)


# calling the function
create_players()

# popup screen
user_answer = screen.textinput(title="Guess the Color",
                               prompt="Who will win the race 'red' 'green' 'blue' 'orange' 'yellow' ")

game = True
# continue the until game variable become false
while game:
    # check u entered the right color or not
    if user_answer in colors:
        # moving all the turtle at a random speed
        for reset in players:
            # random speed from 1 to 10
            speed = random.randint(0, 10)
            # pick up a random turtle
            p1 = random.choice(players)
            # forwarded random turtle by random speed
            p1.forward(speed)

            # the distance of race is 220 if any turtle reached at the last ,it stop
            if p1.xcor() >= 220:
                flag = False
                # pencolor() return the name of turtle who reached first
                winning_color = p1.pencolor()

                # check the user is won or not
                if user_answer == winning_color:
                    tkinter.messagebox.showinfo("Result", "Congratulations, You win the race")
                else:
                    tkinter.messagebox.showinfo("Result",
                                                f"Sorry You lost the race, better luck next time and the answer is {winning_color}")
                # it asks the user, you want to play again or not
                choice = screen.textinput(title="Do you want to play again?",
                                          prompt="Type 'yes' or 'no'")

                # if user choose to play then it start form initial
                if choice == "yes":
                    # reset the turtles
                    for reset in players:
                        reset.goto(x=-230, y=reset.ycor())

                    # taking the user input again
                    user_answer = screen.textinput(title="Guess the Color",
                                                   prompt="Who will win the race 'red' 'green' 'blue' 'orange' "
                                                          "'yellow' ")
                    game = True
                else:
                    game = False


    else:
        tkinter.messagebox.showinfo("Hey", "You entered a wrong color please try again")
        game=False

screen.bye()
