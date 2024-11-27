#1. შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა.
list_1 = [10, 20, 30]
print(len(list_1))
list_2 = [1, 4, 9, 16, 25]
print(len(list_2))
list_3 = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
print(len(list_3))
list_4 = ['red', 'blue']
print(len(list_4))

#2. შექმენთ 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი.
first_list = [ 12, 40, 50]
first_list.append(15)
print(first_list)

second_list =[40 , "apple", "dropshiping"]
second_list.append("codding")
print(second_list)
#3. შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე4ე და მე2ე ადგილას.
list = [3, 7, 15, 22, 41]
list.insert(3 , "goa")
list.insert(1, 30)
print(list)

#4. შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით.
ist =[120, 2540, "watermelon"]
ist.pop(2)
print(ist)
#5. შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში.
languages_1 = ["Python", "Java", "C++", "JavaScript", "Ruby"]
languages_2 = [("Python", 1991), ("Java", 1995), ("C++", 1985), ("JavaScript", 1995), ("Ruby", 1995)]
print(len(languages_1))
print(len(languages_2))
