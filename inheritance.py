#super/parent class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f'hello'
    def parentmethod(self):
        return f'hello from parent method'
#child or subclass
class Dog(Animal):
    def childmethod(self):
        return f'hello from child method'
    def speak(self):
        return f'bark bark'

#add another cat child class
#create a cat object
class Cat(Animal):
    def childmethod(self):
        return f'hello from child method'
    def speak(self):
#add a speak method in cat class
        return f'meow meow'








#create an object
mycat =Cat("Stacy")
print(mycat.name)
#calling a method from superclass
print(mycat.parentmethod())
#overides the parent speak method
print(mycat.speak())
#calling a method inside cat class
print(mycat.childmethod())

#create an object
mydog =Dog("mutwenyoi")
print(mydog.name)
#calling a method from superclass
print(mydog.parentmethod())
#overides the parent speak method
print(mydog.speak())
#calling a method inside dog class
print(mydog.childmethod())













