class Student:
    university = "Oxford"
    def __init__(self,name):
        self.name = name


s1 = Student("John")
s2 = Student("Emma")

print(s1.university)
print(s2.university)

print(Student.university)

# change class variables
Student.university = "MIT"

print(s1.university)
print(s2.university)
