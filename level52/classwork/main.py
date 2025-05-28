def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res

def make_negative(number):
    if number < 0:
        return number
    elif number > 0:
        return -number
    return number  

def DNA_strand(dna):
    result = ''
    for i in dna:
        if i == 'A':
            result += 'T'
        elif i == 'T':
            result += 'A'
        elif i == 'C':
            result += 'G'
        elif i == 'G':
            result += 'C'
    return result