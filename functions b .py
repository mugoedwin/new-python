#function with return keyword returns a value

#function that adds two numbers and returns the
def addTwoNumbers(num1,num2):
    sum=num1+num2
    return sum
#calling the function and storing the returned value in a variable
result=addTwoNumbers(10,20)
print("The sum is",result)
#way 2
print(addTwoNumbers(49,37))
#function that multiplies two numbers
def multiplyTwoNumbs(a,b):
    return a*b
#calling the function
#function that determines even or odd number
def even_or_odd(num):
    if num%2==0:
     return"even"
    else:
     return"odd"
print(even_or_odd(10))
print(even_or_odd(7))
#a function that prints student name and course
def print_student_info(name,course):
    print(f"Student name{name}, your course is {course}")
#calling the function
print_student_info("Najma","FULLSTACK SOFTWARE DEVELOPMENT")

#a function that finds maximum of two numbers
def find_max(a,b):
    if a>b:
        return a
    else:
        return b
#calling function
print(find_max(10,19))





