#Write a program to check if a number is positive or negative.
# num1 = int(input("enter the number for checking if it's it is positive or negative = "))

# if num1 > 0 :
#     print(f"the number is positive {num1} ")
# elif num1 < 0:
#     print(f"the number is negative {num1} ")
# else:
#     print(f"the number is neither positive nor negative {num1}")

#--------------------------------------------------------------------------------------------
#Write a Python program to check whether a number is even or odd using if-else.
# num1 = int(input("enter the number to check whether it's pdd or even = "))
# if num1 % 2 == 0 :
#     print(f" the number is even {num1} ")
# else:
#     print(f"the number is odd {num1}")

#-------------------------------------------------------------------------------------

#Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and
#60, and 'Senior' if 60 or above.
# age = int(input("enter your age = "))
# if age > 0 and age <= 18:
#     print(f" the age is minor {age}")
# elif age > 18 and age <= 60:
#     print(f"the age is of adult {age} ")
# else:
#     print(f" the age is senior citizen { age}")

#-------------------------------------------------------------------------------------

#Write a program that checks if a character entered is a vowel or a consonant.
# Vowels =  a , e ,i , o , u 
# letter = input("enter any alphabet to check whether it's vowel or consonant = ")
# if letter == 'a':
#     print(f" this is a vowel = {letter}")
# elif letter == 'e':
#     print(f" this is a vowel = {letter}")
# elif letter == 'i':
#     print(f" this is a vowel = {letter}")
# elif letter == 'o':
#     print(f" this is a vowel = {letter}")
# elif letter == 'u':
#     print(f" this is a vowel = {letter}")
# else:
#     print(f" the letter is consonant = {letter}")

#-------------------------------------------------------------------------------------
#Write a Python program to check if a number is divisible by 3 and 5 both.

# num1 = int(input("enter the number"))
# if num1 % 3 == 0 and num1 % 5 == 0 :
#     print(f"the number is = {num1} is divisble by 3 and 5 both")
# else:
#     print("the number is not divisible by 3 and 5 ")

#-------------------------------------------------------------------------------------

#Write a Python program to input marks of a student and print the grade: - 90-100 → A - 80-89 →
#B - 70-79 → C - 60-69 → D - <60 → F

# marks = int(input("enter the mark of student so that grade can be assigned to student = "))
# if marks >= 90 and marks <= 100 :
#     print(f" the marks is {marks}, it's grade A")
# elif marks >= 80 and marks <= 89 :
#     print(f" the marks is {marks}, it's grade B")
# elif marks >= 70 and marks <= 79 :
#     print(f" the marks is {marks}, it's grade C")
# elif marks >= 60 and marks <= 69 :
#     print(f" the marks is {marks}, it's grade D")
# else:
#     print(f" the marks is {marks}, it's grade F")

#-------------------------------------------------------------------------------------

#Write a program that takes input for two numbers and prints which one is greater or if they are
#equal.
# num1 = int(input(" enter the 1st number = "))
# num2 = int(input(" enter the 2nd number = "))

# if num1 > num2:
#     print(f" the { num1 }  is greater than {num2}")
# elif num2 > num1:
#      print(f" the { num2 }  is greater than {num1}")
# else:
#      print(f"{num1} is equal to {num2}")


#-------------------------------------------------------------------------------------
#Ask the user to enter a year.
#Convert it into an integer.
#Write a program that checks whether a year is a leap year or not
# leap_year = int(input("enter the year is = "))
# if (leap_year % 400 == 0) or (leap_year % 4 == 0 and leap_year % 4 != 0) :
#     print(f"Yes it is a) leap year = {leap_year}")
# else:
#     print(f" this is not leap year ")


Password = "aditi@123"
user_id = "123456"

enter_password = input("enter the password = ")
enter_user_id = input("enter user Id =")

if user_id == enter_user_id and Password == enter_password:
    print(f"Successfully loggging in....")
else:
    print(f"Unsuccessful login - id or password does not match")


