height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight /(height)**2
print(bmi)

if bmi >= 30: 
    print("Obisity")
elif bmi <= 29 and bmi >= 25:
    print("Overweight")
elif bmi <= 25 and bmi >= 18.5:
    print("Normal")
elif bmi < 18.5:
    print("Underweight")






