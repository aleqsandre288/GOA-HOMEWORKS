# 2) ასაკის ფუნქცია
def check_age(age):
    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
    return age

# 3) სიტყვის ფუნქცია
def check_word(word):
    if word == "":
        raise ValueError("სიტყვა არ უნდა იყოს ცარიელი")
    return word

# 4) ორი რიცხვის ჯამის lambda
sum_lambda = lambda x, y: x + y

# 5) ცელსიუსიდან ფარენჰეიტში lambda და for ციკლი
celsius_list = [0, 10, 20, 30]
c_to_f = lambda c: c * 9/5 + 32
for c in celsius_list:
    print(c_to_f(c))

# 6) map - ყველა რიცხვი გაიზარდოს 5-ით
nums = [3, 6, 9, 12, 15]
increased = list(map(lambda x: x + 5, nums))
print(increased)

# 7) map - ყველა სიტყვა დიდ ასოებად
words = ['hello', 'world', 'python']
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)

# 8) filter - დატოვეთ მხოლოდ რიცხვები რომლებიც მეტია 10-ზე
nums2 = [5, 8, 11, 14, 17]
filtered_nums = list(filter(lambda x: x > 10, nums2))
print(filtered_nums)

# 9) filter - დატოვეთ მხოლოდ სიტყვები, რომლების სიგრძეა >= 5
words2 = ['ant', 'elephant', 'dog', 'giraffe']
long_words = list(filter(lambda w: len(w) >= 5, words2))
print(long_words)

# 10) map და lambda - ყველა რიცხვი გაორმაგდეს
nums3 = [2, 4, 6, 8]
doubled = list(map(lambda x: x * 2, nums3))
print(doubled)

# 11) filter და map ერთად - გაფილტრდეს ლუწები და გაიზარდოს 10-ით
nums4 = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x + 10, filter(lambda x: x % 2 == 0, nums4)))
print(result)
