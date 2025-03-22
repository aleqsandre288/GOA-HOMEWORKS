def greet():
    return "hello world!"

def add_five(num):
    total = num + 5
    return total

def make_negative(number):
    if number < 0:
        return number
    elif number > 0:
        return -number
    return number  

def find_average(numbers):

    if not numbers:
        return 0 

    total = sum(numbers)  
    count = len(numbers)  

    return total / count  
def check_alive(health):
    return health > 0
