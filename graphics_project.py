# import turtle

# pen = turtle.Turtle()

# def ring(col, rad):

# 	pen.fillcolor(col)

# 	pen.begin_fill()

# 	pen.circle(rad)

# 	pen.end_fill()

# pen.up()
# pen.setpos(-35, 95)
# pen.down
# ring('black', 15)

# pen.up()
# pen.setpos(35, 95)
# pen.down()
# ring('black', 15)

# pen.up()
# pen.setpos(0, 35)
# pen.down()
# ring('white', 40)

# pen.up()
# pen.setpos(-18, 75)
# pen.down
# ring('black', 8)

# pen.up()
# pen.setpos(18, 75)
# pen.down()
# ring('black', 8)

# pen.up()
# pen.setpos(-18, 77)
# pen.down()
# ring('white', 4)

# pen.up()
# pen.setpos(18, 77)
# pen.down()
# ring('white', 4)

# pen.up()
# pen.setpos(0, 55)
# pen.down
# ring('black', 5)

# pen.up()
# pen.setpos(0, 55)
# pen.down()
# pen.right(90)
# pen.circle(5, 180)
# pen.up()
# pen.setpos(0, 55)
# pen.down()
# pen.left(360)
# pen.circle(5, -180)
# pen.hideturtle()
# turtle.done()





# import turtle
# t=turtle.Turtle()
# t.penup()
# t.setpos(-20,40)
# t.pendown()
# t.pensize(10)
# t.pencolor("pink")
# t.forward(100)
# t.backward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.backward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# turtle.done()




# import turtle
# colors = [ "pink","yellow","blue","green","white","red"]
# sketch = turtle.Pen()
# turtle.bgcolor("black")
# for i in range(200):
#    sketch.pencolor(colors[i % 6])
#    sketch.width(i/100 + 1)
#    sketch.forward(i)
#    sketch.left(59)




# import turtle

# t = turtle.Turtle()
# t.speed('fastest')

# t.penup()
#t.goto(0, 250)
# t.pendown()

# radius = 40
# angle = 10

# for i in range(36):
#    for j in range(4):
#       t.forward(50)
#       t.right(90)
#    t.penup()
#    t.right(angle)
#    t.forward(radius)
#    t.pendown()

# t.hideturtle()
# turtle.done()






# import turtle
# t = turtle.Turtle()

##SQUARE
# for i in range(4):
#    t.forward(90)
#    t.left(90)

# #RECTANGLEt.forward(side_a)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(90)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(90)

# #CIRCLE
# radius =100
# t.circle(radius)

# #HEXAGON
# for i in range(6):
#    t.forward(200)
#    t.left(300)



# from turtle import *
# import colorsys

# speed(0)
# bgcolor("black")
# h=0
# for i in range(15):
#     for j in range(18): #20
#         c=colorsys.hsv_to_rgb(h,1,1)
#         color(c)
#         h+=0.005
#         rt(90)
#         circle(150-j*6,90)        
#         lt(90)
#         circle(150-j*6,90)
#         rt(180)
#     circle(40,24)
# done()




# import turtle

# # Create a turtle object
# my_turtle = turtle.Turtle()

# # Set the pen color and size
# my_turtle.pensize(3)
# colors = ["red", "blue", "green", "orange"]
# my_turtle.speed(0)
# # Draw a circle pattern
# for i in range(36):
#     my_turtle.pencolor(colors[i % 4])
#     my_turtle.circle(100)
#     my_turtle.right(10)

# # Exit the turtle graphics window
# turtle.done()



# import turtle
# turtle.bgcolor("black")
# t=turtle.Turtle()
# t.speed(0)
# t.pensize(2)
# colors=['red','dark red']
# for num in range(300):
#     t.forward(num+1)
#     t.rt(89)#50,85
#     t.pencolor(colors[num%2])
# t.hideturtle()
# turtle.done()



# import turtle
# t=turtle.Turtle()
# t.color("dark red")
# #t.shape("turtle")
# we=turtle.Screen()
# we.title("shivi creation")
# we.bgcolor("black")
# t.pensize(5)
# t.speed(4)
# t.begin_fill()
# t.fillcolor("dark red")
# t.up()
# t.goto(0,-100)
# t.down()
# t.left(100)
# t.setheading(50)
# t.fd(222)
# t.circle(80,190)
# t.setheading(120)
# t.circle(80,180)
# t.setheading(305)
# t.forward(223)
# t.end_fill()
# t.color("dark red")
# #t.setheading(90)
# #t.forward(100)
# #t.color("white")
# # #t.forward(100)
# # t.backward(50)
# # t.setheading(45)
# # t.fd(60)
# # t.backward(60)
# # t.setheading(-45)
# # t.fd(60)
# t.hideturtle()
# turtle.done()




# import turtle
# s=turtle.Turtle()
# s.color("red")
# p=turtle.Screen()
# p.bgcolor("black")
# s.up()
# s.goto(0,100)
# s.down() 
# s.setheading(243)
# s.fd(200)
# s.bk(200)
# s.setheading(300)
# s.fd(200)
# s.setheading(150)
# s.fd(230)
# s.setheading(0)
# s.fd(210)
# s.setheading(210)
# s.fd(240)
# turtle.done()



# import turtle
# t=turtle.Turtle()
# t.color("black")
# t.pensize(5)
# #t.shape("turtle")
# t.circle(100)
# t.up()
# t.goto(-30,120)
# t.down()
# t.circle(18)
# t.up()
# t.goto(30,118)
# t.down()
# t.circle(18)
# # t.up()
# # t.goto(0,90)
# # t.down()
# # t.setheading(270)
# # t.fd(25)
# # t.circle(10,200)
# # t.up()
# # t.goto(0,65)
# # t.down()
# t.up()
# t.goto(-45,60)
# t.down()
# t.setheading(300)
# t.circle(50,118)
# t.up()
# t.goto(0,0)
# t.down()
# t.setheading(270)
# t.fd(200)
# t.setheading(225)
# t.fd(80)
# t.bk(80)
# t.setheading(315)
# t.fd(80)
# t.bk(80)
# t.setheading(90)
# t.fd(90)
# t.setheading(135)
# t.fd(90)
# t.bk(90)
# t.setheading(45)
# t.fd(90)
# t.hideturtle()
# turtle.done()



# import turtle
# t=turtle.Turtle()
# def ring(col,rad):