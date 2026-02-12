#try ..except
"""
try:
    #block of code that might cause an error
except:
    #code that runs if error happen
"""
try:
    num=int(input("enter a number"))
    print(20/num)
except ZeroDivisionError:
    print("You can not divide a number by zero")
#filenot found
try:
    x=open('abcd.txt','r')
    print(x.read())
except FileNotFoundError:
    print("file not found ")







