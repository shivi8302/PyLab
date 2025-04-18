# a=int(input("enter first number to be adding:"))
# b=int(input("enter second number to be adding:"))

# sum=a+b
# print("sum of {0} and {1} is: {2}" .format(a,b,sum))




# def sum(a,b):
#     return "sum of the number is", a+b
# n=int(input("enter a number:"))
# m=int(input("enter second number:"))
# print(sum(n,m))

# def sum(x,y):
#     if y==0:
#         return x
#     else:
#         return sum(x+1,y-1)
# num1=7
# num2=3
# result=sum(num1,num2)
# print("The sum of",num1,"and", num2,"is", result)




# def table(sum):
#     print("The table of:",sum)
#     for i in range(1,11):
#         print(i,'x',sum, '=', i*sum)
# y=int(input("enter the number for the table:"))
# table(y)

# def print_table(number):
#     print(f"Multiplication table of {number}:")
#     for i in range(1,11):
#         print(f"{number}x{i}={number*i}")
# num=int(input("enter a number:"))
# print_table(num)




#maximum for the two numbers
# a=3
# b=6
# print(a if a>b else b)

# def max(a,b):
#     return a if a>b else b
# x=4
# y=1
# print(max(x,y))

# a=4
# b=5
# k=max(a,b)
# print(k)




# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# a=int(input("enter a number for factorial:"))
# print(factorial(a))

# def factorial(n):
#     return 1 if n==0 or n==1 else n*factorial(n-1)
# a=int(input("enter a number for factorial:"))
# print(factorial(a))




# def simple_interest(P,T,R):
#     simp=(P*T*R)/100
#     print("Your simple interest is :",simp)
# P=int(input("enter principal:"))
# T=int(input("enter time span:"))
# R=int(input("enter interest rate:"))
# simple_interest(P,T,R)


# def compound_interest(P,T,R):
#     A=P*(1 + R/100)**T
#     simp=A-P
#     print("Your compound interest is :",simp)
# P=int(input("enter principal:"))
# T=int(input("enter time span:"))
# R=int(input("enter interest rate:"))
# compound_interest(P,T,R)



# import time
# from datetime import datetime
# input_time = int(input("Enter Your time: "))
# #strp time is used to convert
# time_obj = datetime.strptime(str(input_time),"%H")
# your_time = time_obj.strftime("%H")
# # convert back to int
# your_time = int(your_time)
# if(your_time >= 12 and your_time<=17):
#     print(f"Your entered time {your_time} corresponds to Afternoon")
# elif(your_time>17 and your_time<=21):
#     print(f"Your entered time {your_time} corresponds to Evening")
# elif(your_time>21 and your_time<0):
#     print(f"Your entered time {your_time} corresponds to Night ")
# else:
#     print(f"Your entered time {your_time} corresponds to Morning ")








# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("skyblue")

# # Create a turtle named "tree"
# tree = turtle.Turtle()
# tree.speed(2)

# # Function to draw the tree trunk (a rectangle)
# def draw_trunk():
#     tree.penup()
#     tree.goto(-20, -150)  # Position the turtle at the base of the tree
#     tree.pendown()
#     tree.begin_fill()
#     tree.fillcolor("saddlebrown")
#     for _ in range(2):
#         tree.forward(40)
#         tree.left(90)
#         tree.forward(100)
#         tree.left(90)
#     tree.end_fill()

# # Function to draw the tree foliage (a triangle shape)
# def draw_foliage():
#     tree.penup()
#     tree.goto(-70, -50)  # Position the turtle for the bottom foliage
#     tree.pendown()
#     tree.begin_fill()
#     tree.fillcolor("forestgreen")
#     for _ in range(3):
#         tree.forward(140)
#         tree.left(120)
#     tree.end_fill()

#     # Draw the second layer of foliage
#     tree.penup()
#     tree.goto(-50, 0)  # Position turtle for second foliage layer
#     tree.pendown()
#     tree.begin_fill()
#     tree.fillcolor("darkgreen")
#     for _ in range(3):
#         tree.forward(100)
#         tree.left(120)
#     tree.end_fill()

#     # Draw the third layer of foliage
#     tree.penup()
#     tree.goto(-30, 50)  # Position turtle for the top foliage
#     tree.pendown()
#     tree.begin_fill()
#     tree.fillcolor("lightgreen")
#     for _ in range(3):
#         tree.forward(60)
#         tree.left(120)
#     tree.end_fill()

# # Draw the tree
# draw_trunk()
# draw_foliage()

# # Hide the turtle after drawing
# tree.hideturtle()

# # Finish
# turtle.done()


