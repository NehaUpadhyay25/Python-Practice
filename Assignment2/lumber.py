__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 2
FILENAME : lumber.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program draws different species of trees and then harvest the trees drawn.
It also harvests the trees if clicked below the dividing line in two ways: Sorted
and unsorted. It draws all the logs in a sorted pile on left click and unsorted
on right click. It also computes the total length of the logs.
"""

#imports turtle class for turtle functioning.
#imports random class to use randint function to generate trees chosen randomly each time.
#imports yard class to use its addLog(log) function.

import turtle
import random
import yard

def drawLine(windowWidth,windowHeight):
    """
    Draws dividing line.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (-300,450), heading (east), up
    :param windowWidth: Width of the window.
    :param windowHeight: Height of the window.
    :return: None
    """
    turtle.penup()
    turtle.setposition(-windowWidth/3 , -windowHeight/6)
    turtle.pendown()
    turtle.forward(600)

def buttons(windowWidth,windowHeight):
    """
    Draws two buttons 'Harvest and sort' and 'Harvest unsorted'.
    :pre: (relative) pos (-300,450), heading (east), up
    :post: (relative) pos (112.5,-180), heading (east), up
    :param windowWidth: Width of the window.
    :param windowHeight: Height of the window.
    :return: None
    """
    turtle.penup()
    turtle.setposition(-windowWidth/4, -windowHeight/5)
    turtle.write("Harvest and sort" , font=("10"))
    turtle.setposition(windowWidth/8, -windowHeight/5)
    turtle.write("Harvest unsorted" , font=("10"))

def doclick(x,y):
    """
    Draws trees chosen randomly on x and y coordinates on-click above the dividing
    line and also draws piles of logs when clicked below the dividing line.
    :pre: (relative) pos (112.5,-180), heading (east), up
    :post: (relative) pos (x,y), heading (east), up
    :param x: X-coordinate of the window.
    :param y: Y-coordinate of the window.
    :return: None
    """
    windowHeight = 900
    if y > (-windowHeight / 6):
        if x > -300 and x < 300:
            drawTree(lumberyard,x,y)
            turtle.goto(x,y)

    elif y < (-windowHeight / 6) :
        if x > -300 and x < 300:
            drawLog(lumberyard,x,y)

def drawLog(lumberyard,x,y):
    """
    Draws piles of log in sorted or unsorted way
    when harvested that is clicked below the line.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,10*Number of trees generated), heading (east), up
    :param lumberyard: Object of the class Lumberyard.
    :param x: X-coordinate of the window.
    :param y: Y-coordinate of the window.
    :return: None
    """
    loglist = lumberyard.allLogs()
    totallength = 0
    pileheight = 10
    turtle.hideturtle()

    # draws piles in sorted order
    if x > -300 and x < 0:
        turtle.clearscreen()
        loglist.sort(reverse=True)
        for i in range(len(loglist)):
            turtle.pendown()
            turtle.forward(loglist[i] / 2)
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.left(90)
            turtle.forward(loglist[i])
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.left(90)
            turtle.forward(loglist[i] / 2)
            turtle.penup()
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.right(90)
            totallength = totallength + loglist[i]
        print("The total length of logs is " +str(totallength))
        turtle.exitonclick()


    # draws piles in unsorted order
    else :
        turtle.clearscreen()
        for i in range(len(loglist)):
            turtle.pendown()
            turtle.forward(loglist[i] / 2)
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.left(90)
            turtle.forward(loglist[i])
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.left(90)
            turtle.forward(loglist[i] / 2)
            turtle.penup()
            turtle.left(90)
            turtle.forward(pileheight)
            turtle.right(90)
            totallength = totallength + loglist[i]
        print("The total length of logs is : " +str(totallength))
        turtle.exitonclick()

def drawTree(lumberyard,x,y):
    """
    Draws different species of tree randomly with
    size chosen at random.
    :pre: (relative) pos (112.5,-180), heading (east), up
    :post: (relative) pos (x,y), heading (east), up
    :param lumberyard: Object of the class Lumberyard.
    :param x: X-coordinate of the window.
    :param y: Y-coordinate of the window.
    :return: None
    """
    turtle.setposition(x,y)
    type = random.randint(1,3)
    size = random.randint(50,250)
    log = size

    # draws pine tree with type 1 that is triangle
    if type == 1:

        if (290 - (y + size) >= 50):
            turtle.pendown()
            turtle.left(90)
            turtle.forward(size)
            turtle.right(90)

            turtle.forward(size / 6)
            turtle.left(120)
            turtle.forward(size / 3)
            turtle.left(120)
            turtle.forward(size / 3)
            turtle.left(120)
            turtle.forward(size / 6)
            turtle.penup()
            lumberyard.addLog(log)

    # draws other tree with type 2 that is square
    elif type == 2 :


        if (290 - (y + size + (size / 4)) >= 50):

            turtle.pendown()
            turtle.left(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size / 4)
            turtle.left(90)
            turtle.forward(size / 4)
            turtle.left(90)
            turtle.forward(size / 2)
            turtle.left(90)
            turtle.forward(size / 4)
            turtle.left(90)
            turtle.forward(size / 4)
            turtle.penup()
            lumberyard.addLog(log)

    # draws maple tree with type 3 that is circle
    else :


        if (290 - (y + ( 2 * size)) >= 50):

            turtle.pendown()
            turtle.left(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.circle(size/2)
            turtle.penup()
            lumberyard.addLog(log)

def main():
    """
    The main function which executes all the methods.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    windowHeight = 900
    windowWidth = 900

    drawLine(windowWidth,windowHeight)
    buttons(windowWidth,windowHeight)
    turtle.onscreenclick(doclick)
    turtle.mainloop()

# Executes the main function
if __name__ == '__main__':
    lumberyard  = yard.LumberYard()
    main()

