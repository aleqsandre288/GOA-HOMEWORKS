#1. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მის კვადრატს
num = int(input("enter number to calculate its square: "))
def squarer(num):
    return num*num
print(squarer(num))
#2.შექმენით ფუნქცია, რომელიც არგუმენტად იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.
num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("enter second number: "))
def summer(num1,num2):
    return num1+num2
print(summer(num1,num2))
#3. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს ყველაზე პატარას.
def minnumber(NUM1,NUM2,NUM3):
    NUM1 = int(input("ENTER FIRST NUMBER: "))
    NUM2 =int(input("enter second number: "))
    NUM3 = int(input("enter Third number: "))
    print('your list of numbers: \n')
    List = [NUM1,NUM2,NUM3]
    print(List)
    print('smallest number is:')
    print(min(List))
minnumber('NUM1','NUM2','NUM3')

#4შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და ამოწმებს, არის თუ არა ის დადებითი.
num12 = int(input('enter number :'))
def numdefiner(num12):
    if num12 > 0:
        print('your number is positive')
    elif num12 < 12:
        print("your number is negative")
    elif num12 == 0:
        print('your number is zero')
numdefiner(num12)
# 5. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.
def listsummer(nUM1,nUM2,nUM3):
    nUM1 = int(input("ENTER FIRST NUMBER: "))
    nUM2 =int(input("enter second number: "))
    nUM3 = int(input("enter Third number: "))
    print('your list of numbers: \n')
    List = [nUM1,nUM2,nUM3]
    print(List)
    print('sum of your list is:')
    print(nUM1 + nUM2 + nUM3)
listsummer('nUM1','nUM2','nUM3')
