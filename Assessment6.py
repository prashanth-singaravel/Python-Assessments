Q1:Generate a list of squares for numbers from 1 to 10 using list comprehension.

A1:

squares = [x**2 for x in range(1, 11)]
print(squares)

Q2:Create a list of numbers divisible by 3 from 1 to 30 using list comprehension.

A2:

div_by_3 = [x for x in range(1, 31) if x % 3 == 0]
print(div_by_3)

Q3:Construct a dictionary mapping numbers (1 to 5) to their factorial using dictionary comprehension.

A3:

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

fact_dictionary = {n: fact(n) for n in range(1, 6)}

print(fact_dictionary)

Q4:Generate a dictionary where keys are words from a given list, and values are their lengths.

A4:

words = ['Ocean', 'Sun', 'Earth', 'Sky']
word_len = {word: len(word) for word in words}
print(word_len)

Q5:Create a dictionary that maps numbers from 1 to 10 to 'Even' or 'Odd' using dictionary comprehension.

A5:

number_pair = {num: ('Even' if num % 2 == 0 else 'Odd') for num in range(1, 11)}
print(number_pair)



