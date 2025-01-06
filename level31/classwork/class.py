#1
def add(a,b,c):
    return a + b + c
print(add(2,4 ,8))

def ad(a,b,c):
    print(a + b +c)

print(ad(2,4,8))

#2
list={1,2,3,4,5}
print(list)
guess= int(input("ENTER NUMBER FROM LIST: "))
def secret(secret):
     secret = 4
     if guess == secret:
         print("you won")
     else:
         print("you lost")
print(secret(secret))