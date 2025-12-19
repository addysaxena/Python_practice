
# ----------------------------------------------------------------------------------------------
# P → Principal amount
# r → Rate of interest3
# t → Time (in years)

# P = int(input("Enter the Principal = "))
# R = float(input("Enter the Rate of Interst = "))
# T = int(input("Enter the Duration(In Years) = "))
# A = P * (1 + R/100) ** T
# print(A)

# ----------------------------------------------------------------------------------------------
#BMI = weight / (height * height)


# weight = float(input("Enter the weight in kgs = "))

# height = float(input("Enter the height in meters = "))
# BMI = weight / (height * height)
# if BMI <= 18.5 :
#     print(f"The weight is = {weight} and the BMI is = {BMI} , which is Underweight")
# elif BMI > 18.5 and BMI <= 25 :
#     print(f"The weight is = {weight} and the BMI is = {BMI} , which is Normal")
# elif BMI > 25 and BMI <= 29.9 :
#     print(f"The weight is = {weight} and the BMI is = {BMI} , which is Overweight")
# else:
#     print(f"The weight is = {weight} and the BMI is = {BMI} , which is Obese")

# ----------------------------------------------------------------------------------------------


# basic_salary = float(input("enter the basic salary in rupees = "))
# HRA = basic_salary * (20/100)
# DA = basic_salary * (40/100)
# Total_Salary = basic_salary + HRA + DA

# print(f"The salary in total is = {Total_Salary}")

# ----------------------------------------------------------------------------------------------

# Calculate Discount on a Product
# Product_price = float(input("Enter the Price of the product = "))
# Discount_percentage = int(input("Enter the percentage = "))

# Discounted_price = Product_price * (Discount_percentage/100)
# Final_price = Product_price - Discounted_price 
# print(f" the Discount = {Discounted_price}")
# print(f" the Final price = {Final_price}")

# ----------------------------------------------------------------------------------------------
#Fahrenheit to Celsius: C = (F − 32) * 5/9
# F = int(input("Enter the temperature in Fahrenheit = "))
# C = (F - 32)* 5/9
# print(f"The temperature in celsius = {C}")


# ----------------------------------------------------------------------------------------------
# Electricity Bill Calculator (slab wise)
# 0–100 units → ₹5 per unit
# 101–200 units → ₹7 per unit
# 201–300 units → ₹10 per unit
# Above 300 → ₹12 per unit


# Units = int(input("enter the units that are consumed = "))

# if Units <= 100:
#     print(f"The total Bill will be {Units * 5 } , the slab is  5 rupees per unit")
# elif Units >= 101 and Units <= 200:
#     print(f"The total Bill will be {Units * 7 } , the slab is  7 rupees per unit")
# elif  Units >= 201 and Units <= 300:
#     print(f"The total Bill will be {Units * 10} , the slab is  10 rupees per unit")
# else:
#     print(f"The total Bill will be {Units * 12} , the slab is  12 rupees per unit")


# -------------------------------------------------------------------------------------------
#Calculate Speed = distance / time
# distance = int(input("enter the distance in kms =  "))
# Time = float(input("enter the time in hours = "))
# Speed = distance/Time
# print(f"speed is km/hr = {Speed}")

# 
# Grading System based on average marks- maths

num_1 = float(input("Enter the Marks for 1st student = "))
num_2 = float(input("Enter the Marks for 2st student = "))
num_3 = float(input("Enter the Marks for 3st student = "))

# Marks Range	Grade
# 90–100	A
# 80–89	B
# 70–79	C
# 60–69	D
# Below 60	F
print("the Grade is = ")
if num_1 >= 90 :
    print("Grade A")
elif num_1 >= 89:
        print("Grade B")
elif num_1 >= 79 :
            print("Grade C")
elif num_1 >= 69 :
    print("Grade D")
else :
    print("Grade F")


if num_2 >= 90 :
    print("Grade A")
elif num_2 >= 89:
        print("Grade B")
elif num_2 >= 79 :
            print("Grade C")
elif num_2 >= 69 :
    print("Grade D")
else :
    print("Grade F")

if num_3 >= 90 :
    print("Grade A")
elif num_3 >= 89:
        print("Grade B")
elif num_3 >= 79 :
            print("Grade C")
elif num_3 >= 69 :
    print("Grade D")
else :
    print("Grade F")

