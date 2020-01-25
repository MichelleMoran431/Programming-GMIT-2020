# To Calculate the BMI using height in meters and weight in kg
# Calculation weight/height (in m2)

Height = float(input("Enter Height in meters; "))
Weight = float(input("Enter Weight in kilograms; "))

Heightsquared = (Height*Height)

BMI = Weight/Heightsquared
BMI2=(round (BMI,2))
print ("your BMI is = ", BMI2)

