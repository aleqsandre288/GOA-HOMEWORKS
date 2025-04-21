def solution(string):
    return string[::-1]

def hello(name=""):
    if  not name:
        return "Hello, World!"
    else:
        return "Hello,  " + name.capitalize() + "!"
    

def area_or_perimeter(l , w):
    if  l == w:
        return l*w
    else:
        return 2*l + 2*w
    
def opposite(number):
    return number *-1


def number_to_string(num):
     return str(num)
def square(n):
    return n*n