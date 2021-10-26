# Import all the modules
import turtle
import time
import sys
import winsound as ws

# Creating the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=300,height=200)
wn.title("Digital Clock")
wn.tracer(0)

# Creating the Pens
# Pen 1
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.hideturtle()

# Pen 2
pen2 = turtle.Turtle()
pen2. speed(0)
pen2.penup()
pen2.hideturtle()

# Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()

# Creating a time variable
Time = time.strftime("%H:%M:%S")

# Display the current time and wait for input
print("")
print("Currently it is " + Time + ".")
Alarm = input("Enter the time you want to be notified in hh:mm:ss format: ")
print("")

# Creating the confirmation
print("You will be notified at " + Alarm + ".")
yes_no = str(input("Would you like to set this alarm? [y/n] ")).lower()

# Functions
def draw_clock():
    pen1.pencolor("gray")
    pen1.pensize(5)
    x = pen1.xcor = -75
    y = pen1.ycor = 45
    pen1.goto(x,y)
    pen1.pendown()
    for i in range (2):
        pen1.fd(150)
        pen1.rt(90)
        pen1.fd(50)
        pen1.rt(90)
    pen1.penup()
    pen2.penup()
    pen2.goto(x-15,y+15)
    pen2.pencolor("black")
    pen2.pensize(25)
    pen2.pendown()
    for i in range (2):
        pen2.fd(180)
        pen2.rt(90)
        pen2.fd(80)
        pen2.rt(90)

def clock_time():
    pen3.pencolor("red")
    pen3.goto(0,0)
    pen3.clear()
    pen3.write(h + ":" + m + ":" + s, font=("D", 35, "normal"), align="center")
    pen3.penup()
    pen3.goto(0,-32)
    pen3.pendown()
    pen3.write(d, font=("D",15,"normal"), align="center")

# Main Loops
if yes_no == "n" or yes_no == "no":
    print("")
    print("Currently it is " + Alarm + ".")
    Alarm = input("Enter the time you would like to be notified in hh:mm:ss format: ")
    print("")
    print("You will be notified at " + Alarm + ".")
    yes_no = str(input("Would you like to set the alarm? [y/n] ")).lower()
    print("")

while yes_no == "y" or yes_no == "yes":
    while Time != Alarm:
        Time = time.strftime("%H:%M:%S")
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        d = time.strftime("%D")
        clock_time()
        draw_clock()
        time.sleep(1)
        wn.update()
        if Time == Alarm:
            ws.PlaySound("Alarm Clock Sound", ws.SND_FILENAME)

wn.mainloop()