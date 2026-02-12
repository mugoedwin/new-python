#function- performs a specific task
#def function name:
        #block of code
#creating a function
def greet():
    print("hello good morning")
#calling a function
greet()
greet()
greet()
#another function
def demo():
    print("inazuma eleven ares")
#calling the function
demo()
demo()
demo()
#function with parameters
def greetings(first_name,):
    print("hello greetings",first_name)
#calling the function
greetings("James")
greetings("Bakari")
#function with multiple parameters and a default parameter value
def chrome(name,age=18):
    print(f"hello {name} you are {age} years old")

chrome("Najma",18)
chrome("Mutheu",18)
chrome("John",18)
chrome("Bakari",18)
chrome("Matilda",18)
chrome("James",18)
chrome("Matilda")
chrome("john")

#function that calculates area of a rectangle
def areaofrectangle(l,w):
    area=l*w
    print(f"The area of rectangle with length {l} and width {w} is {area}")
#calling the function
areaofrectangle(10,300)
areaofrectangle(10,300)

#function that calculates area of a circle.3.14*r*r
def areaofcircle(r):
    area=3.14*r*r
    print(f"The area of circle with radius {r} is {area}")
#calling the function
areaofcircle(18)
areaofcircle(19)








