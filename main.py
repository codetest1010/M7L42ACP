import turtle
# create a turtle object
t = turtle.Turtle()
# set screen background color to light blue
screen = turtle.Screen()
screen.bgcolor("lightblue")
# function to draw an equilateral triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)
# function to draw a rectangle
def draw_rectangle():
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
# function to draw a hexagon
def draw_hexagon():
    for _ in range(6):
        t.forward(100)
        t.left(60)
# draw the triangle, fill it with red color
t.fillcolor("red")
t.begin_fill()
draw_triangle()
t.end_fill()
# move turtle to a new position for the rectangle
t.penup()
t.goto(-150, -50)
t.pendown()
# draw the rectangle, fill it with green color
t.fillcolor("green")
t.begin_fill()
draw_rectangle()
t.end_fill()
# move turtle to a new position for the hexagon
t.penup()
t.goto(-200, -150)
t.pendown()
# draw the hexagon, fill it with yellow color
t.fillcolor("yellow")
t.begin_fill()
draw_hexagon()
t.end_fill()
# hide the turtle
t.hideturtle()
# keep the window open until it is closed manually
turtle.done()