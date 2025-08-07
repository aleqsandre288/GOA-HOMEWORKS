def square_sum(numbers):
    return sum(i ** 2 for i in numbers)


def fake_bin(x):
    list = ""
    for i in x:
        if int(i) < 5:
            list += "0"
        if int(i) >= 5:
            list += "1"
            
    return list


def boolean_to_string(b):
    return str(b)