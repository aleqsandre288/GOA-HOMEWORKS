height = float(input("ENTER YOUR HEIGHT: "))
weight = int(input("ENTER YOUR WEIGHT: "))

def bmi(height, weight):
    result = weight / height**2
    return result

bmi_result = bmi(height, weight)
print(f"Your BMI is: {bmi_result}")

underweight = 18.5
normal = 18.5
overweight = 25
obese = 30

if bmi_result < underweight:
    print("YOU ARE UNDERWEIGHT")
elif underweight <= bmi_result < normal:
    print("YOU ARE NORMAL WEIGHT")
elif normal <= bmi_result < overweight:
    print("YOU ARE OVERWEIGHT")
elif overweight <= bmi_result < obese:
    print("YOU ARE OBESE")
else:
    print("YOU ARE EXTREMELY OBESE")
