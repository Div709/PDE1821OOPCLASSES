class Student:
    def __init__(self, name, age,programme):
        # name etc are attributes that we are going to store
        # init means initializing
        # self shows that name is for that specific class
        self.name = name
        self.age = age
        self.programme = programme
    # The above part is for initializing
    # This is usually written once for a class

    def introduce(self):
        print(f'My name is {self.name}.')
        print(f"I study {self.programme}.")
    # introduce() is a function

student1 = Student("Aisha",18,"Robotics") # Here we adding info to the class
student1.introduce() # Here we get student 1's info then using .introduce() to carry out the printing
# student 1 object created
# The info goes to def __init__
import math

class Circle:
    def __init__(self,radius=1):
        self.radius = radius
    def setRadius(self,radius):
        self.radius = radius
    def getArea(self):
        return math.pi*self.radius*self.radius
    def get_circumference(self):
        return 2*math.pi*self.radius
c1 = Circle()
print(c1.radius)
print(c1.getArea())
c1.setRadius(5)
print(c1.radius)
print(c1.getArea())