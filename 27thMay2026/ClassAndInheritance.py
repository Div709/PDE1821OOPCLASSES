class Student:
    def __init__(self, name, age,programme):
        self.name = name
        self.age = age
        self.programme = programme
    def introduce(self):
        print(f'My name is {self.name}.')
        print(f"I study {self.programme}.")
student1 = Student("Aisha",18,"Robotics")
student1.introduce()