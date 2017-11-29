__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 3
FILENAME : antenna.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program implements the shapes recursively.
It implements squares , single line with no gaps
and single line with gaps recursively.
"""


import turtle
import sys

def singleLinerec(size,level,number):
    """
    This method implements the single line recursion either
    with gaps or with no gaps depending on the choice of
    the user.
    :param size: The size of the figure
    :param level: The level upto which the figure should go
    :param number: choice of figure
    """
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    turtle.speed(0)
    turtle.left(135)
    turtle.pendown()
    if(number==2):
        singleLine(size,level)
    else:
        singleLinenogap(size,level)


def singleLine(size, level):
    """
    This method implements the single line recursive function
    with gaps
    :param size: The size of the figure
    :param level: The level of the figure
    """
    singlelineedge(size, level)
    turtle.left(90)
    singlelineedge(size, level)
    turtle.left(90)
    singlelineedge(size, level)
    turtle.left(90)
    singlelineedge(size, level)
    turtle.left(90)

def singleLinenogap(size, level):
    """
    This figure implements single line function with
    no gaps
    :param size: The size of the funtion
    :param level: The level of the recursion
    """
    singlelineedgenogap(size, level)
    turtle.left(90)
    singlelineedgenogap(size, level)
    turtle.left(90)
    singlelineedgenogap(size, level)
    turtle.left(90)
    singlelineedgenogap(size, level)
    turtle.left(90)

def singlelineedge(size,level):
    """
    This is a function which implements the single line function
    with gaps
    :param size: The size of the funtion
    :param level: The level of recursion
    """
    recSize= size/3;
    gapSize= recSize-3;

    if level ==1:
        turtle.fd(size)
        return
    else:
     singlelineedge(recSize,level-1)
     turtle.left(90)
     singlelineedge(gapSize,level-1)
     turtle.right(90)
     singlelineedge(gapSize,level-1)
     turtle.right(90)
     singlelineedge(gapSize,level-1)
     turtle.left(90)
     singlelineedge(gapSize, level -1)

def singlelineedgenogap(size,level):
    """
    This function helps in implementing the single line
    function with no gaps
    :param size: The size of the function
    :param level: The level of recursion
    """
    recSize= size/3;

    if level ==1:
        turtle.fd(size)
        return
    else:
     singlelineedgenogap(recSize,level-1)
     turtle.left(90)
     singlelineedgenogap(recSize,level-1)
     turtle.right(90)
     singlelineedgenogap(recSize,level-1)
     turtle.right(90)
     singlelineedgenogap(recSize,level-1)
     turtle.left(90)
     singlelineedgenogap(recSize, level -1)


def drawSquare(size):
    """
    Draws a square with given size and is called by
    recursive funtion
    :param size: The size of the function
    """
    for i in range(4):

        turtle.forward(size)
        turtle.right(90)

def sofSquaresrec(size,level):
    turtle.left(45)
    sofSquares(size,level)

def sofSquares(size, level):
    """
    The method implements the recursion of squares
    :param size: The size of the figure
    :param level: The level of recursion
    """

    if level == 0:
        drawSquare(size / 3);

    elif level == 1:

        turtle.pendown()
        drawSquare(size / 3)
        turtle.penup()
        turtle.forward(size / 3)
        turtle.left(90)
        turtle.forward(size/3)
        turtle.right(90)
        turtle.pendown()
        drawSquare(size / 3)
        turtle.penup()
        turtle.right(90)
        turtle.forward(2*size / 3)
        turtle.left(90)
        turtle.pendown()
        drawSquare(size / 3)
        turtle.penup()
        turtle.back(2*size / 3)
        turtle.pendown()
        drawSquare(size / 3)
        turtle.penup()
        turtle.left(90)
        turtle.forward(2*size / 3)
        turtle.right(90)
        turtle.pendown()
        drawSquare(size / 3)
        turtle.penup()
        turtle.forward(size/3)
        turtle.right(90)
        turtle.forward(size/3)
        turtle.left(90)


    else:
        turtle.pendown()
        sofSquares(size / 3, level-1)
        turtle.penup()
        turtle.forward(size / 3)
        turtle.left(90)
        turtle.forward(size / 3)
        turtle.right(90)
        turtle.pendown()
        sofSquares(size / 3,level-1)
        turtle.penup()
        turtle.right(90)
        turtle.forward(2 * size / 3)
        turtle.left(90)
        turtle.pendown()
        sofSquares(size / 3,level-1)
        turtle.penup()
        turtle.back(2 * size / 3)
        turtle.pendown()
        sofSquares(size / 3,level-1)
        turtle.penup()
        turtle.left(90)
        turtle.forward(2 * size / 3)
        turtle.right(90)
        turtle.pendown()
        sofSquares(size / 3,level-1)
        turtle.penup()
        turtle.forward(size / 3)
        turtle.right(90)
        turtle.forward(size / 3)
        turtle.left(90)


def main():
    """
    It is the main method and it takes all inputs and calls the desired functions
    """
    turtle.speed(0)
    size = int(input("enter the size you want!"))
    level = int(input("enter the level you want!"))

    if(size < 0):
        print("error in size")
        sys.exit()

    elif(level <0):
        print("error in level")
        sys.exit()
    else:
        print("enter the figure you want 1-squares 2-single line with gaps 3-single line with no gaps")
        number = int(input("enter the choice"))

        if(number == 1):
            sofSquaresrec(size,level)
        elif(number == 2):
            singleLinerec(size,level,number)
        elif(number == 3):
            singleLinerec(size,level,number)
        else:
            print("no choice as that")
        turtle.mainloop()

if __name__ == '__main__':
    main()
