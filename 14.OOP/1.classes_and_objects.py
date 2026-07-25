class Student:
    # attributes
    roll_no = 0
    name = ""
    gender = ""
    age = 0

    def __init__(self,roll_no: int,name: str,age: int,gender: str):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender


    # methods
    def display_details(self):
        print(f"roll_no: {self.roll_no}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")


# instances
student1 = Student(1,"John Doe", 24,"Male")
student2 = Student(2,"Emma Watson", 23, "Female")


student1.display_details()
student2.display_details()



