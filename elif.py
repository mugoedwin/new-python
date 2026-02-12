#elif-to test for multiple condition
"""
if..elif..else
if condition1:
    block of code to be executed if condition1 is true
elif condition2:
    block of code to be executed if condition2 is true
else:
    block of code to be executed if neither conditions are true
"""
#a program that asks user marks then prints the grade
#80-100-A
#70-80-b
#60-70-c
#50-60-d
#else fail
marks=int(input("enter the marks "))
if marks>=80 and marks<=100:
    print("GRADE A")
elif marks>=70 and marks<=80:
    print("GRADE B")
elif marks>=60 and marks<=70:
    print("GRADE C")
elif marks>=50 and marks<=60:
    print("GRADE D")
else:
    print("FAIL")

# a program that asks user for age then
#18-25=young adult
#25-40 adult
#40-60 mature adult
#60>-elderly
#<18-baby

age=int(input("enter your age"))
if age<18:
    print ("baby")
elif age>=18 and age <=25:
    print ("young adult")
elif age>25 and age<=40:
    print ("adult")
elif age>40 and age<=60:
    print ("mature adult")
elif age>60:
    print("mature")




