#n=int(input("enter a number:"))
#print("Writing the table of",n)
#i=1
#while i <= 10:
#    print(n,"x",i,"=", n*i)
#    i+=1
#print("End of table of",n)


#num=[1,4,9,16,25,36,49,64,81,100,]
#x=int(input("enter a number:"))
#ch=0
#for val in num:
#    if (val==x):
#        print("number found at index:",ch)
#    ch+=1


# n=int(input("enter a number:"))
# for i in range(1,11):
#    print(n*i)
 




#Arange the words in albhabetical 
# from functools import reduce 

# def sortString (str):

#   return reduce (lambda a, b : a + b, sorted (str))

# str = input ("Enter a string that you want to arrange in alphabetical order:")

# print (sortString (str))




#def cal_sum(sum):
#    num=30+sum
#    if num%5==0:
#     return num
#    else:
#       print("not calculating")
#    return num
#print(cal_sum(30))
#print(cal_sum(412))
#print(cal_sum(50))




#class Order:
#    def __init__(self,item,price):
#        self.item = item
#        self.price = price
#    def __gt__(self,order2): # __gt__ means 'greater than'
#        return self.price > order2.price    
    
#ord1 = Order("chips",20)
#ord2 = Order("tea",15) 

#print(ord1>ord2)




# def fun(sum,b=6):
#    a=b+sum
#    print(a)
#    return a
# print(fun(10))




#def first5multiples():
# i=1
# while i <=5:
#       print(i,"x",6,"=",(i*6))
#       i+=1   

#print("Hello")
#b=3
#print("Function first5multiples() will print", b+2, "multiples of 6.")
#first5multiples()

# if b+2 >= 5:
#     print("the function printed", b+2, "multiples of 6.")
#     print("python is amazing!")
#     print("i have started")




# n=int(input("Enter a number:"))
# for i in range(1, (n+1)):
#   square = i ** 2
#   #print(f"{i}: {square}")
#   print(i,":",square)





# for i in range(10):
#   print("A", end="")
# for i in range(9):
#   print("B", end="")
# for i in range(8):
#   print("C", end="")
# for i in range(7):
#   print("E", end="")
# for i in range(6):
#   print("F", end="")
# for i in range(5):
#   print("G", end="")
# for i in range(4):
#   print("H", end="")  
# for i in range(3):
#   print("I", end="")
# for i in range(2):
#   print("J", end="")
# for i in range(1):
#   print("K", end="")
# print()










# key='panda'
# correct=False
# while not correct:
#     inp=input("enter secret key:")
#     if inp==key:
#         print("CORRECT! You got that.")
#         break
#     else:
#         print("WRONG guess. Try again.")



# num= int (input("enter the number:"))       
# for i in range(num, 0, -1):
#  #print(" " * (num - i) + "*" * (2 * i - 1))
#  print("*"*i)




#n=8 
#for i in range(1,5):
#    print(n)
#    if i<2:
#        n=int(str(n)+'6')
#    elif i<3:
#        n=int(str(n)+'4')
#    else:
#        n=int(str(n)+'2')



# for i in range(7):
#    if i==0 or i==6:
#        print("#"*7)
#    else:
#        print("#" + " "*5 + "#")

# for i in range(7,0,-1):
#    if i==1 or i==7:
#        print("#"*7)
#    else:
#        print(" "*(i-1) + "#")



#n=int(input("enter the number to be in the list:"))
#b=[]
#for k in range(0,n):
#    a=int(input("Element:"))
#    b.append(a)
#    sum1=0
#    sum2=0
#    sum3=0
#     for i in b:
#         if i>0:
#             if(i%2==0):
#                 sum1=sum1+i
#             else:
#                 sum2=sum2+i
#         else:
#             sum3=sum3+i

# print("sum of all positive even numbers:",sum1)
# print("sum of all psitive odd numbers:", sum2)
# print("sum of all negative numbers:",sum3)



# sum=0
# for i in range(0,10):
#     sum=sum+i
#     print(sum)


# i=0
# for i in range(0,10):
#     i=i+i
#     print(i)



# def fun(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fun(num-2) + fun(num-1)
    
# n=int(input("enter a number:"))
# for i in range(0,n):
#     print(fun(i),end=" ")





# def isPrime(n):
  
#     if(n==1 or n==0):  return False
  
#     for i in range(2,n):
    
#         if(n%i==0):
#             return False
  
#     return True

# N =int(input("enter a number:"))
# for i in range(1,N+1):
#     if(isPrime(i)):
#         print(i,end=" ")




# def num(odds):
#     if odds==1 and odds==0:
#         return 1
#     else:
#         return odds*(odds-1)
# n=int(input("enter a number:"))
# print(num(n))



# #negative indexing
# text="GeeksforGeeks"
# left=text[:-8]
# middle=text[-8:-5]
# right=text[-5:]
# print(left)
# print(middle)
# print(right)

# str='apple'
# print(str[-3:-1])

