"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Jackass will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

jackass = turtle.Turtle()                  # Create a turtle named jackass

jackass.shape('turtle')                    # Set the shape of the turtle to a turtle
jackass.speed(2)                           # Make the turtle move as fast, but not too fast. 
jackass.penup()
jackass.goto(-150, -200)
jackass.pendown()
jackass.pensize(500)
forwards = [ 200, 200, 200, 200, 200, 200, 200 ]
lefts = [ 51.4285714286, 51.4285714286, 51.4285714286, 51.4285714286, 51.4285714286, 51.4285714286, 51.4285714286 ]
colors = [ "green", "red", "yellow", "orange", "purple", "blue", "pink" ]

for i in range(7):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    jackass.color(color)
    jackass.forward(forward)
    jackass.left(left)

turtle.exitonclick()  

