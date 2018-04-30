import turtle
from random import *

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    t.shape("turtle")
    while 1:
	    if sz > 200:
	    	break
	    for j in range (36):
	    	t.left(10)
	    	sz = sz + 1 

	    	if j%2 == 1:
	    		t.color("red")
	    	else:
	    		t.color("blue")
	    	for i in range(4):
	    		t.forward(sz)
	    		t.left(90)
	    sz = sz + 1



def main():                      # Define the main function
    a = raw_input("please enter a box length ")
    b = int(a)
    wn = turtle.Screen()         # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    alex = turtle.Turtle()       # create alex
    alex.speed(0)
    # while 1:
    	# alex.penup()
    	# alex.goto(randint(1,100),randint(1,100))
    	# alex.pendown()
    # a = 10
    drawSquare(alex,b)
    	# a = drawSquare.sz + 1	

	            # Call the function to draw the square
    wn.exitonclick()

main()    