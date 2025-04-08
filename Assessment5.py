# Q1:Write a Python program using a for loop to print numbers from 1 to 10.

# A1:

# for number in range(1, 11):
#     print(number)

# Q2:Write a Python program that takes an integer N as input and uses a while loop to calculate the sum of the first N natural numbers.

# # A2:

# N = int(input("Enter a positive integer N: "))
# sum_of_natural_numbers = 0
# current_number = 1
# while current_number <= N:
#     sum_of_natural_numbers += current_number
#     current_number += 1
# print("The sum of the first", N, "natural numbers is:", sum_of_natural_numbers)

# Q3:Write a Python program that takes an integer as input and prints its multiplication table using a for loop.

# A3:

# num = int(input("Enter an integer: "))
# print(f"Multiplication Table for {num}:")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# Q4:Given a list of numbers, use a loop to count how many numbers are even and how many are odd.

# A4:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_count = 0
# odd_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers count:", even_count)
# print("Odd numbers count:", odd_count)

# Q5:Write a Python program that takes a string as input and prints it in reverse using a loop.

# A5:

# input_string = input("Enter a string: ")
# reversed_string = ""
# for i in range(len(input_string) - 1, -1, -1):
#     reversed_string += input_string[i]
# print("Reversed string:", reversed_string)

# Q6:Write a Python program that takes an integer input and calculates its factorial using a for loop.

# A6:

# def calculate_factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     return factorial

# number = int(input("Enter an integer to calculate its factorial: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = calculate_factorial(number)
#     print(f"The factorial of {number} is {result}.")

# Q7:Write a Python program that prints the first N Fibonacci numbers using a loop.

# A7:

# def print_fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
# n = int(input("Enter the number of Fibonacci numbers to print: "))
# print_fibonacci(n)

# Q8:Write a Python program that checks whether a given number is prime using a loop.

# A8:

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# num = int(input("Enter a number to check whether is it prime: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is a composite number.")

# Q9:Write a program to print the following pattern using nested loops:
# *
# **
# ***
# ****
# *****

# A9:

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print('*', end='')
#     print()

# Q10:Given a list of numbers, write a Python program that finds and prints the largest number using a loop.

# A10:

# numbers = [4, 17, 23, 9, 51, 13, 8]
# max_number = numbers[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num
# print("The largest number is:", max_number)


