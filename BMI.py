# To Calculate the BMI using height in meters and weight in kg
# Calculation weight/height (in m2)

# Ask the user to input their details : 
Height = float(input("Enter Height in meters; "))
Weight = float(input("Enter Weight in kilograms; "))

Heightsquared = (Height*Height) # to calculate metres squared

BMI = Weight/Heightsquared
BMI2=(round (BMI,2)) # to add a round to ensure BMI result is to 2 decimals places after point
print ("your BMI is = ", BMI2) # report the BMI of the user


#def BMI ( Height,Weight):
    #Height = float(input("Enter Height in meters; "))
    #Weight = float(input("Enter Weight in kilograms; "))
    #return round (Weight/Height**2 , 2)