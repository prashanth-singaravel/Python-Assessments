# Q1: Convert the following string into an integer and print its type:
# num_str = "100"

# A1:
# num_str = "100"
# num_int = int(num_str)
# type(num_int)
# print(type(num_int))

# Q2: Convert the following float to an integer and explain the output:
# pi_value = 3.99

# A2:
# pi_value = 3.99
# pi = int(pi_value)
# print(pi)
# print(type(pi))
# Here after float is converted to int, python has ignored the digits after the decimal point. So the value of pi after convering to int has become 3

# Q3: What will be the output of the following code? Why?
# a = 5
# b = "10"
# print(a + int(b))

# A3:
# Output is 15 because the data type of the variable b was converted from string to int before adding it with the variable a and printing the output.

# Q4: Declare variables of type int, float, string, and boolean. Print their values and types.

# A4:
# a = 27
# b = 33.33
# c = "Prashanth"
# d = True
# print(type (a))
# print(type (b))
# print(type (c))
# print(type (d))

# Q5: What will be the output of the following code?
# num1 = "50"
# num2 = 20
# print(num1 + str(num2))

# A5:
# Output is 5020
# Since the integer value 20 stored in the variable num2 is converted to string before adding and printing, addition of 2 strings results in both the strings printed next to each other according to the above given print statement.

# Q6: Write a Python program that asks for the user's name and age, then prints them.

# A6:
# name = input("What is your name? ")
# age = input("What is your age? ")
# print(f"Your name is {name} and you are {age} years old.")

# Q7: What will be the output of the following input-based program if the user enters 25?
# age = input("Enter your age: ")
# print(type(age))
# print(age + 5)

# A7:
# Throws the error integer cannot be concatenated to string.

# Q8: Format the given variables into a single sentence using an f-string.
# name = "Alice"
# age = 22

# A8:
# print(f"Name is {name} and age is {age} years")

# Q9: Rewrite the below statement using .format():
# city = "New York"
# country = "USA"
# print(f"I live in {city}, {country}.")

# A9:
# city = "New York"
# country = "USA"
# print(f"I live in {city}, {country}.".format(country,city))

# Q10: What will be the output of the following print statements?
# print("Hello", "Python", sep="-", end="!")
# print("Next Line")

# A10:
# Hello-Python!Next Line


