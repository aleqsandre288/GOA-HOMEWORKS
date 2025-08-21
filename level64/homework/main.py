

try:
	number = 10
	result = number / 0
except ZeroDivisionError:
	print("ნულზე გაყოფა არ შეიძლება")
	
try:
	my_list = [5, 10, 15]
	print = my_list[5]
except IndexError:
	print("ინდექსი არასწორია, სიაში ასეთი ელემენტი არ არსებობს")




try:
	user_input = input("შეიყვანეთ რიცხვი: ")
	user_number = int(user_input)
except ValueError:
	print("შეიყვანეთ მხოლოდ რიცხვი")


def divide_numbers(a, b):
	try:
		result = a / b
	except ZeroDivisionError:
		print("ნულზე გაყოფა არ შეიძლება")
		return None
	else:
		print("გაყოფა წარმატებით შესრულდა")
		return result

# მაგალითი გამოძახების:
# print(divide_numbers(10, 2))
# print(divide_numbers(5, 0))

def positive_inp(a):
	try:
		a < 0
	except TypeError:
		print("შეიყვანეთ მხოლოდ დადებითი რიცხვი")



# --- 7) try, except, finally ---
try:
	file = open("example.txt", "r", encoding="utf-8")
	content = file.read()
	print("ფაილის შიგთავსი:", content)
except FileNotFoundError:
	print("ფაილი ვერ მოიძებნა")
finally:
	try:
		file.close()
	except Exception:
		pass


# --- 10) სია და int გარდაქმნა შეტყობინებით ---
values = ['10', '20', 'hello', '30']
for v in values:
	try:
		num = int(v)
	except ValueError:
		print(f"მონაცემი არ არის რიცხვი: {v}")

# --- 8) ციკლი სწორი რიცხვის შეყვანისთვის ---
while True:
	try:
		user_input = input("შეიყვანეთ რიცხვი: ")
		user_number = int(user_input)
		break
	except ValueError:
		print("არასწორი შეყვანა, სცადეთ კიდევ ერთხელ")
		

# --- 9) სია და float გარდაქმნა ---
numbers = ["10", "20.5", "abc", "30", "xyz", "40.1"]
float_numbers = []
for item in numbers:
	try:
		float_numbers.append(float(item))
	except ValueError:
		pass
print("სწორად გარდაქმნილი ელემენტები:", float_numbers)





