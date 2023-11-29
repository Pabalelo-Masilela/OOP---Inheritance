'''A logic that determines if the person is 18 or older and create an
instance of the Adult class if this is true. Otherwise, create an instance of the Child class. 
Once the object has been created, call the can_drive() method to print out whether the person is old enough to drive or not.'''

# Class creations
class Adult: 
    def __init__(self,name,age,eye_colour,hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Collecting user inputs for information
name = input("Enter your name:\n")
age = int(input("Enter your age:\n"))
hair_colour = input("Enter your hair colour:\n")
eye_colour = input("Enter your eye colour:\n")
# Logic to determine result to populate based on age
if age < 18:
    person = Child(name, age, hair_colour, eye_colour)
    person.can_drive()
else:
    person = Adult(name, age, hair_colour, eye_colour)
    person.can_drive()