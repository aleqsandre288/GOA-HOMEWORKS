number = [1,4,7,10,13,16,19]
new_list = []
for i in number:
    if i % 2 != 0:
        new_list.append(i*2)
print(new_list)

new__list = (i*2 for i in number if i % 2 != 0)
print(list(new__list))


words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
new_words = []
for i in words:
    if len(i) > 5:
        new_words.append(i)

new = (i for i in words if len(i) > 5)
print(new_words)
print(list(new))

nums = list(range(1, 21))
new_nums = []
for i in nums:
    new_nums.append(i**2)

new_nums_gen = (i**2 for i in nums)
print(new_nums)
print(list(new_nums_gen))


mixed = [2, 5, 8, 11, 14, 17, 20]
even = (i for i in mixed if i % 2 == 0)
odd = (i for i in mixed if i % 2 != 0)
print(list(even))
print(list(odd))

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = []
for animal in animals:
    first_letters.append(animal[0])

first_letters_gen = (animal[0] for animal in animals)
print(first_letters)
print(list(first_letters_gen))