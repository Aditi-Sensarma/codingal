height = int(input("Enter your height(in cm) : "))
weight = int(input("Enter your weight(in KG) : ")) 
BMI = weight/(height**2) 

if BMI < 18.5 :
    print("Underweight")
elif BMI > 18.5 and BMI <24.9 :
    print("Ideal weight")
elif BMI > 25.0 and BMI < 29.9 :
    print("Overweight")
elif BMI > 30.0 and BMI <39.9 :
    print("Obese")
else :
    print("Morbidly obese")