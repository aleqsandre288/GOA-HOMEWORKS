#1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
num = int(input("Enter Number: "))

def add5(num):
    print(num+5)

add5(num)



#2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def multiply(num1, num2):
    print(num1*num2)

multiply(num1,num2)


#3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).
str = str(input("Enter word: "))
def strlen(str):
    print(len(str))
strlen(str)



#4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).
list = ["ale" , "dolidze" , "basketball"]
def lstlen(list):
    print(len(list))
lstlen(list)
#5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.
str1 = input("ENTER WORLD TO CHECK IS IT PALIDROME: ")
def palidrome(str1):
    if str1 == str1[:-1]:
        print("its palidrome")
    else:
        print("its  not")
palidrome(str1)
#6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
#(მაგალითად: input: "Hello World". output: "HELLO WORLD".












