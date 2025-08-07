person = ("joe" , "smith", 30, "new york")

name, surname ,age, city = person
num1 = {1,2,3,4,5,6}
num2 = {4,5,6,7,8,9}
num1.add(10)
num2.remove(9)
intersection = num1.intersection(num2)
union = num1.union(num2)
difference = num1.difference(num2)


student = {
    "name": "Alex",
    "age": 15,
    "grade": "A"
}

print(student.keys())
print(student.values())
print(student.items())

student_copy = student.copy()
print(student_copy)

student.update({"age": 16, "school": "High School"})
print(student)

popped_value = student.pop("grade")
print(popped_value)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

age = student.get("age")
print(age)

height = student.get("height", "Not specified")
print(height)
