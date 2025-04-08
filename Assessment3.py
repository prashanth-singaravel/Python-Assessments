# Q1:Create a list of five numbers. Find and print the sum of all elements.

# A1:

# numbers = [10, 20, 30, 40, 50]
# total_sum = sum(numbers)
# print("The sum of all elements is:", total_sum)

# Q2:Create a tuple of five fruits and print the second and last fruit.

# A2:

# fruits = ("mango", "banana", "cherry", "orange", "grape")
# print("Second fruit:", fruits[1])
# print("Last fruit:", fruits[4])

# Q3:Create a set with five numbers. Add a new number to it and remove an existing number.

# A3:

# numbers = {1, 2, 3, 4, 5}
# numbers.add(6)
# numbers.remove(2)
# print(numbers)

# Q4:Create a dictionary with keys as subjects and values as marks. Print the marks of Mathematics.

# A4:

# marks = {'Mathematics': 95,'Science': 88,'English': 90,'History': 85}
# print("Marks in Mathematics:", marks['Mathematics'])

# Q5:Write a Python program to reverse a list without using the reverse() function.

# A5:

# def reverse_list(lst):
#     reversed_list = []
#     for item in lst:
#         reversed_list = [item] + reversed_list
#     return reversed_list
# original_list = [1, 2, 3, 4, 5]
# reversed_list = reverse_list(original_list)
# print("Original List:", original_list)
# print("Reversed List:", reversed_list)

# Q6:Unpack the elements of a tuple into separate variables and print them.

# A7:

# my_tuple = (10, 20, 30, 40, 50)
# a, b, c, d, e = my_tuple
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)
# print("e:", e)

# Q7:Find the common elements between two sets.

# A7:

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# common_elements = s1.intersection(s2)
# print("Common elements:", common_elements)

# Q8:Add a new subject and its marks to an existing dictionary.

# A8:

# marks = {'Math': 85,'Science': 90,'English': 78}
# print("Current Marks:", marks)
# new_subject = input("Enter the new subject: ")
# new_marks = int(input(f"Enter marks for {new_subject}: "))
# marks[new_subject] = new_marks
# print("Updated Marks:", marks)

# Q9:Given a list of numbers, print only the even-indexed elements.

# A9:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print("Even-indexed elements:")
# for index in range(0, len(numbers), 2):
#     print(numbers[index])

# Q10:Print all keys and values of a dictionary using a loop.

# A10:

# my_dict = {'name': 'Prashanth','age': 27,'city': 'Chennai'}
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")
