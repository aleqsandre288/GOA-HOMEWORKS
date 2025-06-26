#1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების ჩამონათვალს და აბრუნებს ახალ სიას, სადაც თითოეული რიცხვი მრავლდება 2-ზე, for loop და .append()-ის გამოყენებით.7
number = [1, 2, 3, 4, 5]

def multiply_by_two(number):
    result = []
    for i in number:
        result.append(i*2)
    return result
print(multiply_by_two(number))
#2. შექმენით პროგრამა, სადაც მომხმარებელს შეატანინებთ რიცხვს 5-ჯერ, დაამატებთ მათ სიაში და დაბეჭდავთ შებრუნებულ სიას.
numbers = []
for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)
print("შებრუნებული სია:", numbers[::-1])
#3. შექმენით ფუნქცია, რომელიც მიიღებს სიტყვების ჩამონათვალს და დააბრუნებს მათი სიგრძის სიას.
def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
words_list = ["apple", "banana", "cherry"]
print(word_lengths(words_list))
#4. შექმენით პროგრამა, რომელიც ახდენს მარტივი სკოლის ჟურნალის სიმულაციას, მიიღეთ სტუდენტების სახელები და ქულები input()-ით, დაამატეთ ისინი სიაში და აჩვენეთ თითოეული მოსწავლის სახელი მის გვერდზე საშუალო ქულით.
students = []
while True:
    name = input("შეიყვანეთ სტუდენტის სახელი (დასრულებისთვის დააწერეთ 'დასრულება'): ")
    if name.lower() == 'დასრულება':
        break
    score = float(input(f"{name}-ის ქულა: "))
    students.append((name, score))
    for students, score in students:
        print(f"{students} - საშუალო ქულა: {score:.2f}")

#5. შექმენით ფუნქცია, რომელიც მიიღებს სტრინგების სიას და დააბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ 3 სიმბოლოზე მეტ სტრინგებს.
def filter_long_strings(strings):
    long_strings = []
    for string in strings:
        if len(string) > 3:
            long_strings.append(string)
    return long_strings


