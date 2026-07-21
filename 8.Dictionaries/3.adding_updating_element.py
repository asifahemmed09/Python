student = {
    "name": "John Doe",
    "age": 32,
    "gender": "Male"
}

print(student,id(student))

# add a element
student["city"] = "New York"
print(student,id(student))

# update a element
student["age"] = 24
print(student)

# update multiple element
student.update({"age":26,"city":"California"})
print(student)
