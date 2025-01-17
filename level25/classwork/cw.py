a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOMD NUMBER: "))
operation = input("ENTER OPERATION: ")
if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)

password = "bazinga"
guess = input("TRY AND GUESS THE PASSWORD: ")
while guess != password:
    print("TRY AGAIN")
    break
