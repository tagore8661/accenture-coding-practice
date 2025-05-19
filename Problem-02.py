#A person’s body mass index is a simple calculation based on height and weight that classifies the person as underweight, overweight, or normal. The formula for metric unit is,

def BMI_Category(weight,height):
    BMI = weight / (height * height)

    if BMI < 18 :
        return 0
    elif BMI >=18 and BMI < 25 :
        return 1
    elif BMI >=25 and BMI < 30 :
        return 2
    elif BMI >=30 and BMI < 40 :
        return 3
    else:
        return 4
    
weight = 64
height = 1.52

print(BMI_Category(weight,height))