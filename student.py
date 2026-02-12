#class is a blueprint for creating of:
#object-is an instance of a class
#objects-attributes and methods
#student attributes:what it has-name,age,course
#method-what it can do
from encodings.punycode import selective_find
from tkinter.constants import MITER


class Student:
    #constructor
    #it is automatically called when creating an object
     def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

     def __str__(self):
        return f'name is {self.name}, age is {self.age}, course is {self.course}'

     def getemail(self):
        return f'{self.name} @emobilis.co.ke'
     #a method that displays student name and course
     def display_info(self):
         return f'The student is {self.name}, and they are learning {self.course}'
#creating an object
#objectname=class name(values)
student1=Student("MARY",17,"MIT")
print(student1)
#another object
student2=Student("Calvin",18,"Python")
print(student2)
#another object
student3=Student("Najma",22,"CSS")
print(student3)
#another object
student4=Student("James",25,"C++")
print(student4)

#accessing the value
print(student1.name)
print(student2.age)
print(student3.course)
#calling the getemail()
print(student1.getemail())
print(student2.getemail())
print(student3.getemail())

#calling the display_info()
print(student1.display_info())
print(student2.display_info())
print(student3.display_info())
print(student4.display_info())





















