username = input("Enter your name: ")
print("*"*20)
print(f"{username} welcome to my store")
print("*"*20)
print("*"*10 + "Items Available in our store" + "*"*10)

print("Cartoon Astronaut T-shirt[0] : $78")
print("Cartoon Astronaut T-shirt[1] : $78")
print("Cartoon Astronaut T-shirt[2] : $78")
print("Cartoon Astronaut T-shirt[3]: $78")
print("Cartoon Astronaut T-shirt[4] : $78")
print("Cartoon Astronaut T-shirt[5] : $78")
print("Cartoon Astronaut Pants[6] : $178")
print("Cartoon Astronaut T-shirt[7] : $78")

list = ["T-shirt1", "T-shirt2", "T-shirt3", "T-shirt4", "T-shirt5", "T-shirt6", "pants", "T-shirt8"]

choice = input("Do you want to proceed shopping?(yes/no): ")
if choice == "yes":
    user_chose = int(input("Choose an item (0-7): "))
elif choice == "no":
    print("Thanks for visiting us, goodbye")
    

add = input("Do you want to add something else?(yes/no): ")
cart = []  # Create an empty list to store chosen items
cart.append(list[user_chose])  # Add the initially chosen item to the cart

while add == "yes":
    user_chose2 = int(input("Choose an item (0-7): "))
    if user_chose2 == 0:
        print(f"You added {list[0]} in your cart")
    elif user_chose2 == 1:
        print(f"You added {list[1]} in your cart")
    elif user_chose2 == 2:
        print(f"You added {list[2]} in your cart")
    elif user_chose2 == 3:
        print(f"You added {list[3]} in your cart")
    elif user_chose2 == 4:
        print(f"You added {list[4]} in your cart")
    elif user_chose2 == 5:
        print(f"You added {list[5]} in your cart")
    elif user_chose2 == 6:
        print(f"You added {list[6]} in your cart")
    elif user_chose2 == 7:
        print(f"You added {list[7]} in your cart")
    
    cart.append(list[user_chose2])  # Add the second chosen item to the cart
      # Exit the loop after the second item is chosen
    break
print("Your cart contains:", cart)

