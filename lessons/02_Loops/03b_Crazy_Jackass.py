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


forwards = jackass.forward(23)
lefts = [ 45, -60, 90, 45, -90, 60, 22 , -45 ]
colors = [ "green, red, cyan, yelow, purple, pink, lime, orange" ]

for  i in range(8):

    forward = forwards
    left = lefts
    color = colors


    jackass.color(colors)
    jackass.forward(forwards)
    jackass.left(lefts)

turtle.exitonclick()  

