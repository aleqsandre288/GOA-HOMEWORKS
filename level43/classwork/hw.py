def count_positives_sum_negatives(arr):


    if not arr:
        return []
    positive = 0
    negative= 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i
    return [positive , negative]


def get_volume_of_cuboid(length, width, height):
    return length * width * height

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)