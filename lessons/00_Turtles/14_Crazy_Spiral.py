"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import random
import turtle
... # Copy code to make a turtle and set up the window
turtle.setup (width=600, height=600) 
window = turtle.Screen()


t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    for i in range(4):
        t.forward(100)
        t.left(45)
        t.forward(50)
        t.left(45)
        t.forward(50)


def make_a_shape2(t):
    for i in range(3):
        t.forward(250)
        t.left(120)
               
    t.circle(10)
colors = [ 'red', 'blue', 'black', 'orange']    

        




# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.
colors = [ 'red', 'blue', 'green', 'orange', 'pink', 'purple', 'yellow', 'cyan', 'crimson', 'violet', 'magenta', 'lime', 'black', 'brown', 'tan', 'cornflower blue', 'olive', 'dark orange', 'papaya whip', 'gray', 'salmon', 'chocolate', 'coral', 'maroon', 'indian red', 'misty rose', 'linen', 'thistle', 'orchid', 'dark orchid', 'medium orchid', 'tomato', 'aquamarine', 'dark slate gray', 'teal', 'dark slate blue', '', '', '' ] 
num_shapes = 200
for i in range(100):
    t.color(colors[i%len(colors)])
    make_a_shape2(t)
    t.right(360/num_shapes)
turtle.done()