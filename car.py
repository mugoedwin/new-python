#car=color,model,engine,make
class Car:
    def __init__(self,brand,color,engine,):
        self.brand = brand
        self.color = color
        self.engine = engine

    def display_info(self):
        return f'The car is a {self.brand}  {self.color} in color with a {self.engine} engine'
#creating an object
car1 =Car('honda','blue',engine='honda')
print(car1.display_info())
#creating an object
car2 =Car('mercedes','white',engine='twin turbo')
#creating an object
car3 =Car('Mustang','navy blue','electric')
#creating an object
car4 =Car('BMW','maroon','hellish')
#accessing the object attribute
print(car1.brand)
print(car1.engine)
print(car2.brand)
print(car2.engine)
print(car3.brand)
#calling the display info
print(car1.display_info())
print(car2.display_info())
print(car3.display_info())
print(car4.display_info())




