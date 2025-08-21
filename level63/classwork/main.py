# 1-იდან 20-მდე რიცხვების სია (ვრცელი გზა)
numbers = []
for i in range(1, 21):
    numbers.append(i)
print("1-20:", numbers)

# 10-იდან 40-მდე მხოლოდ ლუწი რიცხვების სია (ვრცელი გზა)
even_numbers = []
for i in range(10, 41):
    if i % 2 == 0:
        even_numbers.append(i)
print("ლუწი 10-40:", even_numbers)

# 1-იდან 8-მდე რიცხვების კვადრატების სია (ვრცელი გზა)
squares = []
for i in range(1, 9):
    squares.append(i ** 2)
print("კვადრატები 1-8:", squares)

# იგივე მოკლე გზით (list comprehension)
numbers2 = [i for i in range(1, 21)]
even_numbers2 = [i for i in range(10, 41) if i % 2 == 0]
squares2 = [i ** 2 for i in range(1, 9)]
print("1-20 (მოკლე):", numbers2)
print("ლუწი 10-40 (მოკლე):", even_numbers2)
print("კვადრატები 1-8 (მოკლე):", squares2)

# კენტ რიცხვები 5-იდან 15-მდე, გამრავლებული ორზე (მოკლე გზით)
odds_times_two = [i * 2 for i in range(5, 16) if i % 2 == 1]
print("კენტი 5-15 *2:", odds_times_two)
