# Q1:Write a Python program to check if a number is positive, negative, or zero.

# A1:

# a = int(input("Enter the number : "))
# if a == 0:
#     print(f"The Entered number {a} is Zero.")
# if a > 0:
#     print(f"{a} is a Positive Number.")
# if a < 0:
#     print(f"{a} is a Negative Number.")

# Q2:Write a program to check if a number is even or odd.

# A2:

# a = int(input("Enter the number : "))
# if a % 2 == 0:
#     print(f"{a} is an Even number.")
# else:
#     print(f"{a} is an Odd number.")

# Q3:Write a Python script to find the largest of three numbers.

# A3:

# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))
# if (n1 >= n2) and (n1 >= n3):
#     largest = n1
# elif (n2 >= n1) and (n2 >= n3):
#     largest = n2
# else:
#     largest = n3
# print(f"The largest number among {n1} , {n2} & {n3} is {largest}")

# Q4:Write a program that checks if a character is a vowel or consonant.

# A4:

# char = input("Enter a alpabetic character : ")
# vowels = "aeiouAEIOU"
# if len(char) != 1:
#     print("Entered input is not a single alphabetic character.")
# else:
#     if char in vowels:
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is a consonant.")

# Q5:Check if a number is a multiple of both 3 and 5.

# A5:

# num = int(input("Enter a number : "))
# if (num % 3 == 0) & (num % 5 == 0):
#     print(num, "is divisible by both 3 & 5")
# else:
#     print(num, "is not divisible by both 3 & 5")

# Q6:Write a Python program to check if a year is a leap year.

# A6:

# year = int(input("Enter the year : "))
# if year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# Q7:Take an age as input and print whether the person is a child, teenager, adult, or senior citizen.

# A7:

# a = int(input("Enter age of the person :"))
# if ((a >=1)&(a<=12)):
#     print (a,"is a Child")
# if ((a >=13)&(a<=19)):
#     print(a,"is a Teenager")
# if ((a >=20)&(a<=70)):
#     print(a,"is an Adult")
# if (a >70):
#     print(a,"is a Senior Citizen")

# Q8:Write a Python program to print the absolute value of a number.

# A8:

# number = int(input("Enter a number: "))
# if number < 0:
#     absolute_value = -number
# else:
#     absolute_value = number
# print(f"The absolute value of {number} is {absolute_value}.")

# Q9:Check if a user-provided number is a prime number.

# A9:

# num = int(input("Enter a number: "))

# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{num} is a Prime number.")
# else:
#     print(f"{num} is a Composite number.")

# Q10:Write a Python program that categorizes a given temperature as Cold, Warm, or Hot based on a threshold.

# A10:

# COLD_THRESHOLD = 15
# HOT_THRESHOLD = 30

# temp = int(input("Enter the temperature in Degree Celcius : "))

# if temp < COLD_THRESHOLD:
#     category = "Cold"
# elif COLD_THRESHOLD < temp < HOT_THRESHOLD:
#     category = "Warm"
# else:
#     category = "Hot"
# print(f"{temp} degree Celcius is {category}.")
