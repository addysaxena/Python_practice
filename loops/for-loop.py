# students =["aditi","prabhat", "prachi", "shailja", "dhruv"]
# for student in students:
#     print(student)
#     if student == "prachi":
#         break


# students =["aditi","prabhat", "prachi", "shailja", "dhruv"]
# for student in students:
 
#     if student == "prachi":
#         continue
#     print(student)



# principal = float(input("Enter principal amount: "))
# years = int(input("Enter number of years: "))

# total_si = 0

# for year in range(1, years + 1):
#     rate = float(input(f"Enter rate for year {year}: "))
#     si = (principal * rate) / 100
#     total_si += si

# print("Total Simple Interest:", total_si)
# print("Final Amount:", principal + total_si)


principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (years): "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI:", round(emi, 2))