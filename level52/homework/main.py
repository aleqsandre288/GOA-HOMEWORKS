def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"


def is_divisible(n,x,y):
    fits_x = n // x
    
    back_x = fits_x * x == n

    
    fits_y = n // y
    back_y = fits_y * y == n

    
    if back_x and back_y:
        return True
    else:
        return False