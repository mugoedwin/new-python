#conditional statements
"""
if statement--specifies a block of code to be executed if a given condition is true
if condition:
     block of code to be  executed if condition is true
"""
m=10
if m<20:
    print(f"{m} is less than 20")
#if...else
"""
if condition:
    block of code to be  executed if condition is true
else:
    block of code to be  executed if condition is false
"""

age=12
if age>=18:
     print("you are eligible to vote")
else:
     print("you are not eligible to vote")
#get user input and check if they are eligible to drive
user_age =int(input("enter your age"))
if user_age>=18:
     print("you can drive")
else:
     print("you are not eligible to drive")
# a program that asks user to enter a number
#a and checks if number is even or odd evennum%2=0
num=int(input("enter a number"))
if num%2==0:
     print(f"{num} is an even number5")
else:
     print(f"{num} is an odd number")

# a program that asks user for two numbers
# and checks the greater of the two numbers
# a program that asks users for numbers and checks if its
#positive,negative or zero

number=int(input("enter a number:"))
if number>1:
     print("positive number")
elif number<=-1:
     print("negative number")
else:
     print("zero")








