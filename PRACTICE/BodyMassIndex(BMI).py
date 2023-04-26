def BMI_of_people(weight, height):
    BMI = weight/(height**2)
    return BMI

weight = 76
height = 1.75
BMI = BMI_of_people(weight, height)
print("BMI is", BMI)