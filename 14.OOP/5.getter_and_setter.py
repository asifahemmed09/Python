class Student:
    def __init__(self,name):
        self.__name = name

    # getter
    @property
    def name(self):
        return self.__name
    # setter
    @name.setter
    def name(self,name):
        self.__name = name


s1 = Student("John")
print(s1.name)

s1.name = "Jane"

print(s1.name)
