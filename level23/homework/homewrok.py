#1. შექმენი ცვლადი, სადაც შეინახავ სტრინგს, შემდეგ გამოიტანე იმ სტრინგის მეორე ასო.
word="world"
print(word[1])
#2. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
num1=14
num2=15
print(int(num1+num2))
#3. შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).
a= "basket"
b="ball"
print(a+b)
#4. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
first= 30
second= 15
print(first/second)
#5. გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
print('hello')
num="15"
print(int(num) + 20)

for i in range(4):
    print("hello")

Nam= 20
while Nam< 25:
    print(Nam) 
    Nam += 1
 
#6. შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
print(3*15==13*12)

#7. გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)
 #== : Equal to (e.g., a == b)
 #!= : Not equal to (e.g., a != b)
 #> : Greater than (e.g., a > b)
 #< : Less than (e.g., a < b)
 #>= : Greater than or equal to (e.g., a >= b)
 #<= : Less than or equal to (e.g., a <= b)
#8. შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი
a = 10
b = 5
c = 20


if a > b and c > a:
    print("Both conditions are True")
else:
    print("At least one condition is False")


#9. შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.

for i in range(1,10):
    print(i)
#10. შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
numbers = [1, 2, 3, 4, 5]

# Initialize a variable to store the sum
total = 0

# Loop through the list and add each number to the total
for num in numbers:
    total += num

# Print the total sum
print(total)

#11. შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
string= "hello wrold"
for i in string:
    print(i)
#12. შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
i=1
while i < 10:
    print(i)
    i += 1
#13. შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
num = 1  

while num <= 100:
    if 50 <= num <= 60:
        num += 1
        continue 
    print(num)
    num += 1

#14. შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს
total = 0  
nim = 1    

while total < 50:
    total += nim  
    nim += 1      


print("Total sum:", total)


