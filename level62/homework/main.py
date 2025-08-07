person = ("Alex", 15, "Georgia")

name, age, country = person

print(name)
print(age)
print(country)


# თავდაპირველი სია
my_list = ["apple", "banana", "cherry"]

# სიიდან tuple-ის შექმნა
my_tuple = tuple(my_list)

# tuple-დან სიად გადაქცევა
new_list = list(my_tuple)

# ბეჭდვა
print("საწყისი სია:", my_list)           # ['apple', 'banana', 'cherry']
print("გადაყვანილი tuple:", my_tuple)   # ('apple', 'banana', 'cherry')
print("თავიდან სია:", new_list)          # ['apple', 'banana', 'cherry'



# Set-ის შექმნა
numbers = {1, 3, 5}

# ორი რიცხვის დამატება add() მეთოდით
numbers.add(7)      # 7 დაემატა
numbers.add(9)      # 9 დაემატა

# ორი ელემენტის წაშლა remove() მეთოდით
numbers.remove(1)   # 1 წაიშალა
numbers.remove(3)   # 3 წაიშალა

print("numbers:", numbers)  # დარჩენილი ელემენტები

# მეორე set-ის შექმნა
even_numbers = {2, 4, 6, 8, 9}

# ორ set-ს შორის გაერთიანება (ყველა უნიკალური ელემენტი)
union_set = numbers.union(even_numbers)
print("union:", union_set)

# ორი set-ის გადაკვეთა (რომელიც ორივეშია)
intersection_set = numbers.intersection(even_numbers)
print("intersection:", intersection_set)

# განსხვავება (რა არის numbers-ში, რაც არ არის even_numbers-ში)
difference_set = numbers.difference(even_numbers)
print("difference:", difference_set)
def modify_set(s):
    s.add(10)
    s.add(20)
    s.add(30)
    s.remove(10)
    return s

# მაგალითი
my_set = {1, 2, 3}
result = modify_set(my_set)
print(result)



# Dictionary-ის შექმნა student
student = {
    "name": "Alex",
    "hobby": "basketball",
    "height": 185,
    "weight": 70
}

# .get() მეთოდით name-ის მიღება (უსაფრთხოდ)
student_name = student.get("name")
print("Name:", student_name)

# .pop() მეთოდით height-ის წაშლა და მიღება
removed_height = student.pop("height")
print("Removed height:", removed_height)

# საბოლოო dictionary
print("Final student dict:", student)


def get_keys_values(d):
    keys = d.keys()       # აბრუნებს ყველა key-ს
    values = d.values()   # აბრუნებს ყველა value-ს
    print("Keys:", keys)
    print("Values:", values)
    return keys, values

# მაგალითი ლექსიკონისთვის
student = {
    "name": "Alex",
    "age": 15,
    "grade": "A"
}

# ფუნქციის გამოძახება
get_keys_values(student)


# ლექსიკონის შექმნა
person = {
    "name": "Nino",
    "age": 25,
    "country": "Georgia"
}

# .items() აბრუნებს key-value წყვილებს tuple-ის სახით
for key, value in person.items():
    print(key, ":", value)  # თითოეული წყვილი იბეჭდება ცალკე ხაზზე
