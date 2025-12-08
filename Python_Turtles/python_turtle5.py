import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Sunflower Using Turtle")

t = turtle.Turtle()
t.speed(0)
t.width(2)

def draw_petal(color):
    t.color(color)
    t.begin_fill()
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    t.end_fill()

h = 0.1
for i in range(18):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    draw_petal(c)
    t.right(20)
    h += 0.04

t.hideturtle()
turtle.done()
