# 3. Your BMI Calculator:

print("Your BMI calculator")
height = input('Enter your height here in m: ')
weight = input('Enter your weight here in kg: ')
bmi = float(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

