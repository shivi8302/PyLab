import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Rose Flower")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

num_colors = 36
colors = [colorsys.hsv_to_rgb(i/num_colors, 1, 1) for i in range(num_colors)]

k = 7
size = 200

for layer in range(6):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for angle in range(0, 360 * 2):  
        theta = math.radians(angle)
        r = size * math.sin(k * theta) * (0.8 + layer*0.05)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        r_col, g_col, b_col = colors[(angle // 20) % num_colors]
        pen.pencolor(r_col, g_col, b_col)
        pen.goto(x, y)

pen.penup()
pen.goto(0, -30)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

pen.penup()
pen.goto(-50, -200)
pen.pendown()
pen.color("green")
pen.begin_fill()
pen.circle(100, 120)  
pen.end_fill()

pen.penup()
pen.goto(50, -200)
pen.pendown()
pen.begin_fill()
pen.circle(100, -120)  
pen.end_fill()


pen.hideturtle()
turtle.done()

