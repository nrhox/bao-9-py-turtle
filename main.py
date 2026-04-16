import turtle
import random
import math

t = turtle.Turtle()
t.speed(0)

colors = [
    "#C69C00",
    "#2980B9",
    "#CB4335",
    "#16A085",
    "#7D3C98",
    "#008080",
    "#4B0082",
    "black",
]


def setUpTurtle(x=-250, y=-150):
    t.penup()
    t.goto(x, y)
    t.pendown()


def drawTriagle(size=70):
    t.color(random.choice(colors))
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.forward(size)


def setNextLayer(current_triagle, size=70):
    t.penup()
    backward_distance = (size * current_triagle) - (size / 2)
    t.backward(backward_distance)

    height = size * 0.87
    t.left(90)
    t.forward(height)
    t.right(90)
    t.pendown()


def drawPiramida(fondasi, lebas_segitiga):
    height_triagle = 1 / 2 * 70 * math.sqrt(3)

    setUpTurtle(-(fondasi * lebas_segitiga / 2), -(fondasi / 2 * height_triagle))
    current_target_triagle = fondasi

    for _ in range(fondasi):
        for _ in range(current_target_triagle):
            drawTriagle(lebas_segitiga)

        if current_target_triagle > 1:
            setNextLayer(current_target_triagle, lebas_segitiga)
            current_target_triagle -= 1
        else:
            break


drawPiramida(11, 70)
turtle.done()
