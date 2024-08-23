
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

fatguy = turtle.Turtle()                  # Create a turtle named fat guy

fatguy.shape('turtle')                    # Set the shape of the turtle to a turtle
fatguy.speed(2)                           # Make the turtle move as fast, but not too fast. 
fatguy.goto(-250, 0)
def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        fatguy.forward(100)                              # Move the fat guy forward by the forward distance
        fatguy.left(angle)                              # Turn the fat guy left by the left turn


draw_polygon(4)                        # Draw a square

fatguy.forward(200)                                     # Move the fat guy to another spot on the screen

draw_polygon(5)                        # Draw a pentagon

fatguy.forward(200)                                     # Move the fat guy to another spot on the screen

draw_polygon(6)                        # Draw a hexagon

fatguy.forward(200)

turtle.exitonclick()                     # Close the window when we click on it
