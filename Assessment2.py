Q1:Write a Python program to calculate the area of a circle given the radius.

A1:

r = float(input("Enter the radius of the circle: "))
a =((22*r*r)/7)
print(f"The area of the circle with radius {r} is {a:.2f}")

Q2:Take two numbers as input and check if the first number is greater than the second.

A2:

num_1 = int(input("Enter the first number :"))
num_2 = int(input(("Enter the second number :")))
if num_1 > num_2:
    print(num_1,"is greater than",num_2)
else:
    print(num_1,"is less than",num_2)

Q3:Write a Python program to check if a number is both even and divisible by 5.

A3:

num=int(input("Enter a number : "))
if (num % 5 == 0)&(num % 2 == 0):
    print (num, "is an even number and divisibe by 5 ")
elif(num % 5 == 0):
    print (num, "is divisibe by 5 ")
elif(num % 2 == 0):
    print (num, "is an even number ")
else:
    print(num,"is neither an even number nor divisble by 5")

Q4:Start with x = 10, then increment it by 5, divide it by 3, and print the final value.

A4:

x = 10
x += 5
x /= 3
print(x)

Q5:Write a program to find the bitwise AND and OR of two numbers.

A5:

num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter the second number :"))

bitwise_and_value = num_1 & num_2
print("AND",bitwise_and_value)
bitwise_or_value = num_1 | num_2
print("OR",bitwise_or_value)


Q6:Write a program to swap two numbers without using a third variable.

A6:

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
print(f"Before swapping: First number = {a}, Second Number = {b}")
a, b = b, a
print(f"After swapping: First number = {a}, Second Number = {b}")

Q7:Check if a given year is a leap year using only comparison operators.

A7:

year = int(input("Enter the year : "))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

Q10:Compute (a + b) * c / d taking user input values.

Q8:Write a program that takes two boolean values as input and prints their and, or, and not results.

A8:

a = input("Enter first boolean value (True/False): ").strip().lower() == "true"
b = input("Enter second boolean value (True/False): ").strip().lower() == "true"

if a and b:
    print(f"AND operation: {a} AND {b} = {a and b}")
print(f"OR operation: {a} OR {b} = {a or b}")
if not a and b:
    print(f"NOT operation: NOT {a} = {not a}, NOT {b} = {not b}")

Q9:Given x = 15, use +=, -=, *=, and /= operators to modify x and print the final value.

A9:

x = 15
x += 5
x -= 3
x *= 2
x /= 4

print(x)

A10:

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
d = int(input("Enter the value of d :"))
result = (a+b)*c/d
print(f"{a}+{b}*{c}/{d}={result}")
