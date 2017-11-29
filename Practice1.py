import turtle

def drawface(radius):
    turtle.right(90)
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(radius)
    turtle.penup()
    turtle.home()

    '''   drawnose()

    turtle.left(180)
    turtle.penup()
    turtle.forward(radius-100)
    turtle.right(90)
    turtle.forward(radius - 80)
    turtle.right(90)
    turtle.pendown()

    draweyes()

    turtle.penup()
    turtle.forward(radius-100)
    turtle.left(90)
    turtle.forward(radius-80)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.pendown()

    draweyes()

    turtle.penup()
    turtle.right(90)
    turtle.home()
    turtle.pendown()  '''

    drawhair(radius)


def draweyes():

    for i in range(3):
        turtle.forward(15)
        turtle.left(120)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawnose():
    turtle.penup()
    turtle.right(90)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.pendown()
    for i in range(3):
        turtle.forward(40)
        turtle.left(120)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawhair(radius):

    start = 50
    stop = 150
    step = 5
    hairlength = 55
    turtle.penup()
    turtle.left(start)
    turtle.forward(radius)
    turtle.pendown()
    for i in range(start, stop, +20):
        turtle.forward(hairlength)
        turtle.penup()
        turtle.backward(hairlength + radius)
        turtle.left(i)
        turtle.pendown()


def main():
    radius=180
    drawface(radius)

if __name__ == '__main__':
    main()
    turtle.mainloop()


