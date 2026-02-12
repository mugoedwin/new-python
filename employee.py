#employee class
class Employee:
    def __init__(self,name,salary):
      self.name = name
      self.salary =salary
    def __str__(self):
     return f'my name is {self.name} and my salary is {self.salary}'
Registry = Employee("Mugo", 5000)
print(Registry)
Registry = Employee("Mwangi", 8000)
print(Registry)
Registry = Employee("Edwin", 5000)
print(Registry)