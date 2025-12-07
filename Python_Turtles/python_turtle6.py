import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#EAF6FF")   
t = turtle.Turtle()
t.speed(3)


t.penup()
t.goto(0, -200)
t.pendown()
t.color("#5c3a21")
t.pensize(15)
t.left(90)
t.forward(120)

t.pensize(8)
branches = [(60, 45), (40, -30), (50, -50)]
for length, angle in branches:
    t.right(angle)
    t.forward(length)
    t.backward(length)
    t.left(angle)

t.color("#FFC0CB")   
t.pensize(1)

def blossom(x, y):
    """Draws a tiny cherry blossom."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.circle(6)
        t.right(72)
    t.end_fill()

for _ in range(30):
    x = random.randint(-90, 120)
    y = random.randint(-50, 160)
    blossom(x, y)

t.penup()
t.goto(-100, 200)
t.color("#ff5e9c")
t.write("Cherry Blossom 🌸", font=("Arial", 18, "bold"))

t.hideturtle()
turtle.done()
