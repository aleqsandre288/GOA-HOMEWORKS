# 1. ZeroDivisionError
# ხდება, როდესაც რიცხვს ვყოფთ ნულზე
# მაგალითი:
# x = 5 / 0

# 2. ValueError
# ხდება, როდესაც ფუნქციას გადაეცემა არასწორი მნიშვნელობა
# მაგალითი:
# num = int("abc")

# 3. TypeError
# ხდება, როდესაც ოპერაცია არასწორი ტიპის ობიექტზე სრულდება
# მაგალითი:
# result = 5 + "hello"

# 4. IndexError
# ხდება, როდესაც სიის არარსებულ ინდექსზე მივდივართ
# მაგალითი:
# lst = [1, 2, 3]
# print(lst[5])

# ValueError-ის დამუშავება try, except, finally-ის მეშვეობით:
try:
    num = int("abc")  # აქ მოხდება ValueError
except ValueError:
    print("მნიშვნელობა არ შეიძლება გარდაიქმნას რიცხვად!")
finally:
    print("ეს ბლოკი ყოველთვის შესრულდება.")

# 2) პროდუქტების სია, მომხმარებლის ინდექსის შემოწმება და error handling
products = ["პური", "რძე", "ყველი", "კვერცხი", "შაქარი"]
try:
    user_input = input("შეიყვანეთ პროდუქტის ინდექსი: ")
    index = int(user_input)
    if index >= len(products):
        raise IndexError("ასეთი ინდექსი არ არსებობს პროდუქტების სიაში!")
    print(f"თქვენ აირჩიეთ: {products[index]}")
except ValueError:
    print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი!")
except IndexError as e:
    print(e)
