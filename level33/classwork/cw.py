#1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.

user = input('ENTER YOUR NAME : ')

def reversespeller(user):
    print('\n your name spelled reversly :')
    for letter in user[::-1]:
        print(letter)
reversespeller(user)

#2. შექმენით ფუნქცია, რომელსაც გადაეცემა 5 არგუმენტი, 5 ინფუთით მომხარებელს აარჩევინეთ ნებისმიერი რიცხვი, ბოლოს კი დაუპრინტეთ ამ რიცხვებისაგან შემდგარი სია.

def yourlist(num1,num2,num3,num4,num5):
    num1= int(input("enter number: "))
    num2= int(input("enter number: "))
    num3= int(input("enter number: "))
    num4= int(input("enter number: "))
    num5= int(input("enter number: "))
    list=[num1,num2,num3,num4,num5]
    print("YOUR LIST IS " )
    print(list)
yourlist("num1","num2","num3","num4","num5")
    
#3. შექმენით ფუნქცია რომელიც არგუმენტად აიღებს თქვენს შექმნილ სიას, რომელშიც იქნება მინიმუმ 5 რიცხვი და დაპრინტავს ამ სიისის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და სიის სიგრძეს.

def listanalisis(num6,num7,num8,num9,num10):
    num6= int(input("enter number: "))
    num7= int(input("enter number: "))
    num8= int(input("enter number: "))
    num9= int(input("enter number: "))
    num10= int(input("enter number: "))
    lists=[num6,num7,num8,num9,num10]
    print("YOUR LIST IS " )
    print(lists)
    highest_number = max(lists)
    minimum_number = min(lists)
    print(highest_number)
    print(minimum_number)
    print(len(lists))
    
    
listanalisis("num6","num7","num8","num9","num10")