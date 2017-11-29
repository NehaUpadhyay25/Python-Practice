__author__ = 'nxu3128'

"""
CSCI 603-02: Assignment 1
File: myname.py
Author: Neha Upadhyay nxu3128@rit.edu

Description: Code prints my family name 'UPADHYAY'.  It also makes uses the feature of function reuse.
"""

# imports turtle class for turtle functioning and math function for drawing diagonal lines
import turtle
import math

# global constants to set Window Size
WINDOW_WIDTH =  800
WINDOW_HEIGHT = 800

# Function to set Window size
def windowCoordinates():
    """
    Set window coordinates to ( -100, -400) is in the lower left and
    (500, 400) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    turtle.setworldcoordinates(-100, -WINDOW_WIDTH/2, 500, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.hideturtle()
    turtle.title('Name')
    turtle.speed(0)

# Function to draw Full Name
def drawName():
    """
    Draw the name.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (410,0), heading (east), right
    :return: None
    """

    drawU()
    drawSpace()
    drawP()
    drawSpace()
    drawA()
    drawSpace()
    drawD()
    drawSpace()
    drawH()
    drawSpace()
    drawY()
    drawSpace()
    drawA()
    drawSpace()
    drawY()
    drawSpace()

# Function to draw character 'U'
def drawU():
    """
    Draw character U.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (30,0), heading (east), right
    :return: None
    """

    turtle.down()

    turtle.left(90)
    turtle.forward(60)
    turtle.right(180)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(180)
    turtle.penup()
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()

# Function to draw character 'P'
def drawP():
    """
    Draw character P.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (30,0), heading (east), right
    :return: None
    """

    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()


# Function to draw character 'A'
def drawA():
    """
    Draw character A.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (30,0), heading (east), right
    :return: None
    """

    turtle.penup()
    turtle.back(10)
    turtle.pendown()
    val = math.sqrt(math.pow(15,2) + math.pow(60,2))
    turtle.left(70)
    turtle.forward(val)
    turtle.right(140)
    turtle.forward(val)
    turtle.backward(val / 2)
    turtle.right(110)
    turtle.forward(20)
    turtle.back(20)
    turtle.left(110)
    turtle.penup()
    turtle.forward(val / 2)
    turtle.left(70)
    turtle.pendown()

# Function to draw character 'D'
def drawD():
    """
    Draw character D.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (30,0), heading (east), right
    :return: None
    """

    val = math.sqrt(math.pow(5,2) + math.pow(20,2))
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(30)
    turtle.forward(val)
    turtle.right(60)
    turtle.forward(40)
    turtle.right(65)
    turtle.forward(val)
    turtle.right(23)
    turtle.forward(20)
    turtle.right(182)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()

# Function to draw character 'H'
def drawH():
    """
    Draw character H.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (30,0), heading (east), right
    :return: None
    """

    turtle.left(90)
    turtle.forward(60)
    turtle.penup()
    turtle.back(30)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()

# Function to draw character 'Y'
def drawY():
    """
    Draw character Y.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (35,0), heading (east), right
    :return: None
    """

    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(35)
    turtle.left(45)
    turtle.forward(33)
    turtle.backward(33)
    turtle.right(90)
    turtle.forward(33)
    turtle.backward(33)
    turtle.left(45)
    turtle.backward(35)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

# Function to include space after every character printed
def drawSpace():
    """
    Draw Spaces.
    :pre: pos (0,0), heading (east), right
    :post: pos (20,0), heading (east), right
    :return: None
    """

    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

# Main Function
def main():
    """
    The main function
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    windowCoordinates()
    drawName()

    turtle.mainloop()

# Executes the main function
if __name__ == "__main__":
    main()