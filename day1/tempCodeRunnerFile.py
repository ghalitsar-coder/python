weight = 95
height = 1.77

bmi = weight / (height ** 2)

if bmi  < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else : 
    print("overweight")